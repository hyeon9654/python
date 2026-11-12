# [역할] 예측 로직 파일: 학습된 Pipeline 로드 → DataFrame 변환 → predict → 결과 반환
# 수업 참고: day16/Service.py의 클래스, 생성자, self, 메서드, 서비스 객체 생성
import math
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline


class RecoveryService:
    def __init__(self):
        # 생성자는 RecoveryService()로 객체를 만들 때 한 번 실행합니다.
        # self.변수는 같은 객체의 다른 메서드에서도 사용하는 멤버변수입니다.
        # 실행한 터미널 위치와 관계없이 이 파일 옆 models 폴더를 사용합니다.
        self.model_path = Path(__file__).resolve().parent / "models" / "recovery_model.pkl"
        self.metrics_path = Path(__file__).resolve().parent / "models" / "recovery_metrics.pkl"
        self.columns = [
            "Age", "Gender", "Training_Duration_Min", "Training_Intensity",
            "Sleep_Duration_Hours", "Stress_Level", "Caffeine_Intake_mg", "Muscle_Soreness",
        ]
        # 처음에는 비워 두고, 최초 예측 요청 때 파일을 읽습니다.
        self.model = None
        self.metrics = None

    def load_model(self):
        # 파일이 없으면 오류를 전달합니다. API에서 학습하거나 가짜 값을 만들지 않습니다.
        # 최초 예측 시 로드하며, 정상 로드 후 같은 객체를 재사용합니다.
        # joblib.load(): 파일로 저장한 학습 Pipeline을 파이썬 객체로 복원합니다.
        model = joblib.load(self.model_path)
        metrics = joblib.load(self.metrics_path)

        # [모델 검증 보완] 다른 과제의 모델이나 잘못된 지표를 연결하지 않도록 확인합니다.
        if not isinstance(model, Pipeline):
            raise ValueError("전처리를 포함한 학습 Pipeline이 필요합니다.")
        if list(getattr(model, "feature_names_in_", [])) != self.columns:
            raise ValueError("모델의 원본 입력 컬럼과 API 컬럼 순서가 다릅니다.")
        if not isinstance(metrics, dict) or metrics.get("input_columns") != self.columns:
            raise ValueError("성능 지표 파일의 입력 컬럼이 모델 규격과 다릅니다.")
        if metrics.get("target_column") != "Recovery_Score":
            raise ValueError("회복 점수 모델의 평가 지표가 아닙니다.")
        r2 = metrics.get("r2_score")
        mae = metrics.get("mae")
        if not isinstance(r2, (int, float)) or not math.isfinite(r2) or r2 > 1:
            raise ValueError("저장된 테스트 R2 점수가 올바르지 않습니다.")
        if not isinstance(mae, (int, float)) or not math.isfinite(mae) or mae < 0:
            raise ValueError("저장된 테스트 MAE 점수가 올바르지 않습니다.")
        self.model = model
        self.metrics = metrics

    def predict(self, data):
        # 1. 조회: 저장된 Pipeline과 테스트 성능 지표를 준비합니다.
        if self.model is None:
            self.load_model()

        # 2. 변환: null은 numpy 결측값으로만 바꿉니다. 중앙값 대체는 Pipeline 담당입니다.
        row = {}
        for column in self.columns:
            value = data.get(column)
            if value is None:
                row[column] = np.nan
            else:
                row[column] = value
        # row는 한 명의 입력 딕셔너리, [row]는 그 한 행을 담은 리스트입니다.
        # columns를 지정하여 학습 당시 컬럼 이름과 순서를 맞춥니다.
        df = pd.DataFrame([row], columns=self.columns)
        # 범주형 값이 모두 미입력인 한 행도 범주형 열로 유지합니다.
        for column in ["Gender", "Stress_Level"]:
            df[column] = df[column].astype(object)

        # 3. 예측: 학습 때 저장한 동일한 전처리와 Ridge 모델을 사용합니다.
        predictions = self.model.predict(df)
        # 한 행을 넣었으므로 첫 번째 예측값 [0]을 사용합니다.
        # float()는 numpy 숫자를 JSON 응답에 사용할 파이썬 실수로 변환합니다.
        raw_prediction = float(predictions[0])
        if not math.isfinite(raw_prediction):
            raise ArithmeticError("모델이 유한하지 않은 회복 점수를 예측했습니다.")
        # 표시 점수만 0~100으로 제한하고 원본 예측값과 보정 여부를 구분합니다.
        score = raw_prediction
        if score < 0:
            score = 0.0
        elif score > 100:
            score = 100.0

        warnings = []
        for column, limits in self.metrics["training_ranges"].items():
            value = data.get(column)
            if value is not None:
                if value < limits["min"] or value > limits["max"]:
                    warnings.append(f"{column}: 학습 데이터 범위({limits['min']}~{limits['max']}) 밖의 입력입니다.")
        missing_count = 0
        for column in self.columns:
            if data.get(column) is None:
                missing_count += 1
        if missing_count >= 4:
            warnings.append("선택 항목 7개 중 4개 이상이 미입력되어 예측의 신뢰도가 낮아질 수 있습니다.")

        # 4. 반환: R2/MAE는 현재 요청에서 계산하지 않고 저장된 테스트 평가값을 읽습니다.
        return {
            "predicted_recovery_score": score,
            "raw_prediction": raw_prediction,
            "score_was_clipped": score != raw_prediction,
            "r2_score": float(self.metrics["r2_score"]),
            "mae": float(self.metrics["mae"]),
            "warnings": warnings,
        }


# 수업 예제의 item_service = ItemService()와 같은 구조입니다.
# Controller는 이 객체를 import해서 recovery_service.predict()를 호출합니다.
recovery_service = RecoveryService()
