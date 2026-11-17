# A/B 병렬 개발 순서

## A: Java / React
- A02: build.gradle WebFlux/Validation 수정 및 Spring 실행
- A03: application.properties (8080, ai.server.url)
- A04: PredictionRequestKrw DTO (19개)
- A05: CurrencyService (금액 13개 KRW→TWD)
- A06~A07: POST /api/predict/start, 요청 ID 임시 보관
- A08: MockSseController 테스트
- A09~A10: WebClient POST /predict/stream, GET /api/predict/events/{id} 중계
- A11~A14: React 입력, Axios, EventSource, 결과/위험 요인
- A15: 전체 테스트 및 발표

## B: Python
- B01: data CSV 확인, 19개 피처/타깃 선정
- B02: LightGBM + Optuna 학습과 F1
- B03: joblib 저장
- B04: FastAPI /predict/stream
- B05: 기여도 기반 위험 요인 Top3 (선택)
- B06: Java 연동 및 테스트

## 통합 우선순위
1. Java `/health` 실행
2. Python `/health` 실행
3. Java `GET /api/mock/events` 확인
4. Python `/predict/stream` 실제 SSE 출력 확인
5. Spring WebClient 스트리밍 중계 연결
6. React Axios POST → EventSource SSE → DONE 카드
