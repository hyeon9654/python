package com.example.creditguard.controller;

import com.example.creditguard.dto.PredictionRequestKrw;
import com.example.creditguard.dto.PredictionStartResponse;
import com.example.creditguard.service.PredictionService;
import jakarta.validation.Valid;
import org.springframework.http.MediaType;
import org.springframework.http.codec.ServerSentEvent;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Flux;

@RestController
@RequestMapping("/api/predict")
@CrossOrigin(origins = "http://localhost:5173")
public class PredictController {
    private final PredictionService service;

    public PredictController(PredictionService service) {
        this.service = service;
    }

    // A06: React에서 Axios로 원화 데이터를 전송합니다.
    @PostMapping("/start")
    public PredictionStartResponse start(@Valid @RequestBody PredictionRequestKrw request) {
        return new PredictionStartResponse(service.start(request));
    }

    // A10: React에서 EventSource로 SSE를 구독합니다.
    @GetMapping(value = "/events/{requestId}", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> events(@PathVariable String requestId) {
        return service.stream(requestId);
    }
}
