# CreditGuard 폴더·파일 틀 설치 안내

## 권장 위치
기존 `python` 저장소 폴더의 **최상위**에 프로젝트 3개를 병렬 배치하세요.

- `creditguard-backend/`: 기존 Spring Boot 프로젝트 **유지**. 기존 `build.gradle` 및 `gradlew.bat`은 변경하지 않음
- `creditguard-ai/`: Python 팀원 담당 FastAPI + 모델 학습
- `creditguard-frontend/`: React + Axios + SSE
- `docs/`: API 계약 및 담당자 단계표

## 설치 방법 (Windows VS Code 터미널)
1. 이 ZIP을 `python` 루트에 압축 해제합니다. `setup_creditguard.py`, `templates/`이 보여야 합니다.
2. 터미널이 `python` 루트인지 확인한 뒤 `python .\setup_creditguard.py` 실행.
3. 스크립트는 없는 파일만 생성하며 기존 파일은 **덮어쓰지 않습니다**.
4. `creditguard-backend`에서 `build.gradle` 의존성을 WebFlux/Validation으로 변경합니다.
5. 기존에 있던 `Controller/HeanthController.java`를 `controller/HealthController.java`로 이름과 위치를 변경합니다. 기존 파일 삭제 전에 코드 보관 및 중복 클래스 여부를 확인하세요.
6. `application.properties`에 `server.port=8080`과 `ai.server.url=http://localhost:8000` 설정.
7. Spring에서 `./gradlew.bat clean build` 및 `./gradlew.bat bootRun` 테스트.

## 주의
- 이 패키지는 **기본 뼈대**입니다. Java의 CurrencyService/PredictionService와 Python 모델 학습은 TODO 상태입니다. 주석 및 테스트 응답을 실제 구현으로 착각하지 마세요.
- Python의 `/predict/stream`은 미구현일 때 `ERROR` 상태를 반환합니다. 실제 AI 예측은 아직 되지 않습니다.
- `UCI_Credit_Card.csv`는 팀원이 `creditguard-ai/data/`에 복사해서 사용하세요. GitHub로 CSV를 올릴 필요는 없습니다.
- Python 팀원 작업 파일이 이미 있다면 스크립트가 건너뛰도록 설계했습니다.

## Git 주의
- 기존 최상위 `.gitignore`는 `*.csv`만 들어 있을 수 있습니다. 최상위 `.venv/`를 Git에 올리지 않도록 루트 `.gitignore`에 `.venv/`, `__pycache__/`, `node_modules/`를 추가하세요.
