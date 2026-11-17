import axios from 'axios';

const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8080';

// A11: 원화 입력값을 Spring에 전송하고 requestId를 반환받습니다.
export async function startPrediction(input) {
    const response = await axios.post(`${BASE_URL}/api/predict/start`, input);
    return response.data.requestId;
}

// A12: SSE의 data JSON을 읽습니다. status = VALIDATING / PREPROCESSING / PREDICTING / DONE / ERROR
export function openPredictionStream(requestId, onData, onError) {
    const source = new EventSource(`${BASE_URL}/api/predict/events/${encodeURIComponent(requestId)}`);
    source.onmessage = (event) => {
        const data = JSON.parse(event.data);
        onData(data);
        if (data.status === 'DONE' || data.status === 'ERROR') source.close();
    };
    source.onerror = (error) => {source.close(); if (onError) onError(error);};
    return source;
}
