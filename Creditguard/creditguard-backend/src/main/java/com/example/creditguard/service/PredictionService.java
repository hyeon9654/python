package com.example.creditguard.service;

import com.example.creditguard.dto.PredictionRequestKrw;
import org.springframework.http.codec.ServerSentEvent;
import org.springframework.stereotype.Service;
import reactor.core.publisher.Flux;

@Service
public class PredictionService {
    // A07 TODO: requestId별 입력값 임시 보관 및 사용 완료 시 제거
    public String start(PredictionRequestKrw request) {
        throw new UnsupportedOperationException("A07 TODO: 요청 ID 생성/저장");
    }

    // A09-A10 TODO: WebClient POST /predict/stream 호출 및 SSE 중계
    public Flux<ServerSentEvent<String>> stream(String requestId) {
        return Flux.error(new UnsupportedOperationException("A09-A10 TODO: WebClient 및 SSE 중계"));
    }
}
