package com.example.creditguard.service;

import com.example.creditguard.dto.PredictionRequestKrw;
import com.example.creditguard.dto.PredictionRequestTwd;
import org.springframework.stereotype.Service;
import java.math.BigDecimal;

@Service
public class CurrencyService {
    // A05 TODO: KRW 금액 13개만 TWD로 변환하고, PAY 상태 6개는 변경하지 않습니다.
    // 시연용 고정 환산율(실시간 시장 환율 아님): 1 TWD = 40.5 KRW
    private static final BigDecimal KRW_PER_TWD = new BigDecimal("40.5");

    public PredictionRequestTwd toTwd(PredictionRequestKrw request) {
        throw new UnsupportedOperationException("A05 TODO: 원화 환산 로직 구현");
    }
}
