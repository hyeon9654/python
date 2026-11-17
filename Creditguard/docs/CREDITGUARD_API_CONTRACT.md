# CreditGuard — API 계약 (Java A / Python B)

## 공통 규격
- React → Spring: KRW 입력 19개, POST `/api/predict/start` → `{"requestId":"..."}`
- React → Spring: GET `/api/predict/events/{requestId}` (EventSource)
- Spring → FastAPI: POST `/predict/stream`, 19개 원본 CSV 컬럼명, TWD 입력
- Python 응답: `text/event-stream`, **event 필드 없이** `data: {"status":"..."}` 사용
- 상태: `VALIDATING`, `PREPROCESSING`, `PREDICTING`, `DONE`, `ERROR`
- DONE: `prediction`, `label`, `probability`, `risk_level`, `f1` (추가 `risk_factors` 선택)
- 환산: 금액 13개만 Java에서 KRW÷40.5 (시연 고정값), PAY 상태 6개는 변환하지 않음

## 모델 입력 19개
`LIMIT_BAL`, `PAY_0`, `PAY_2`, `PAY_3`, `PAY_4`, `PAY_5`, `PAY_6`, `BILL_AMT1`, `BILL_AMT2`, `BILL_AMT3`, `BILL_AMT4`, `BILL_AMT5`, `BILL_AMT6`, `PAY_AMT1`, `PAY_AMT2`, `PAY_AMT3`, `PAY_AMT4`, `PAY_AMT5`, `PAY_AMT6`

타깃: `default.payment.next.month` (Python 모델 학습에서만 사용)

### DONE 예시 (가상 데이터)
```text
data: {"status":"DONE","prediction":1,"label":"채무불이행 위험","probability":0.78,"risk_level":"HIGH","f1":0.49}

```

**주의:** UI 원화 환산은 대만 2005년 데이터를 한국 최신 금융 모델로 바꾸지 않습니다. `prediction`과 `risk_level`은 구분해야 합니다. 위험 등급은 시연용 정책입니다.
