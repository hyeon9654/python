from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import json

app = FastAPI(title="CreditGuard AI Server")

@app.get("/health")
def health():
    return {"status": "OK", "service": "creditguard-ai"}

# B04 TODO: 19개 JSON 입력 검증 -> 저장된 모델 추론 -> 상태별 SSE 반환
# 경로/형식은 공통 API 명세에 맞췄으며, 모델 예측은 아직 구현하지 않았습니다.
@app.post("/predict/stream")
def predict_stream(payload: dict):
    def generate():
        message = {"status": "ERROR", "message": "B04 TODO: 모델 추론 미구현"}
        yield f"data: {json.dumps(message, ensure_ascii=False)}\n\n"
    return StreamingResponse(generate(), media_type="text/event-stream")
