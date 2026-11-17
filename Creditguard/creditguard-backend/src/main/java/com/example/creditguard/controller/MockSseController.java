package com.example.creditguard.controller;

import org.springframework.http.MediaType;
import org.springframework.http.codec.ServerSentEvent;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

// A08: 실제 Python 서버가 준비되기 전, SSE 데이터 구조만 점검합니다.
@RestController
public class MockSseController {
    @GetMapping(value = "/api/mock/events", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> mockEvents() {
        return Flux.just(
                ServerSentEvent.<String>builder().data("{\"status\":\"VALIDATING\",\"message\":\"Mock 검증 중\"}").build(),
                ServerSentEvent.<String>builder().data("{\"status\":\"PREPROCESSING\",\"message\":\"Mock 전처리 중\"}").build(),
                ServerSentEvent.<String>builder().data("{\"status\":\"PREDICTING\",\"message\":\"Mock 예측 중\"}").build(),
                ServerSentEvent.<String>builder().data("{\"status\":\"DONE\",\"prediction\":0,\"label\":\"Mock 정상\",\"probability\":0.1,\"risk_level\":\"LOW\",\"f1\":0.5}").build()
        );
    }
}
