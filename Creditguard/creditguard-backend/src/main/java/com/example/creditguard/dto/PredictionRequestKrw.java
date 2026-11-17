package com.example.creditguard.dto;

import jakarta.validation.constraints.NotNull;
import java.math.BigDecimal;

// A04: React에서 받은 KRW 금액 13개 + 상환 상태 6개를 보관합니다.
public record PredictionRequestKrw(
        @NotNull BigDecimal limitBalKrw,
        @NotNull Integer pay0,
        @NotNull Integer pay2,
        @NotNull Integer pay3,
        @NotNull Integer pay4,
        @NotNull Integer pay5,
        @NotNull Integer pay6,
        @NotNull BigDecimal billAmt1Krw,
        @NotNull BigDecimal billAmt2Krw,
        @NotNull BigDecimal billAmt3Krw,
        @NotNull BigDecimal billAmt4Krw,
        @NotNull BigDecimal billAmt5Krw,
        @NotNull BigDecimal billAmt6Krw,
        @NotNull BigDecimal payAmt1Krw,
        @NotNull BigDecimal payAmt2Krw,
        @NotNull BigDecimal payAmt3Krw,
        @NotNull BigDecimal payAmt4Krw,
        @NotNull BigDecimal payAmt5Krw,
        @NotNull BigDecimal payAmt6Krw
) {}
