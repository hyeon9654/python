package com.example.creditguard.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import java.math.BigDecimal;

// A05: FastAPI에 보낼 CSV 원본 컬럼명 19개 (금액은 TWD).
public record PredictionRequestTwd(
        @JsonProperty("LIMIT_BAL") BigDecimal limitBal,
        @JsonProperty("PAY_0") Integer pay0,
        @JsonProperty("PAY_2") Integer pay2,
        @JsonProperty("PAY_3") Integer pay3,
        @JsonProperty("PAY_4") Integer pay4,
        @JsonProperty("PAY_5") Integer pay5,
        @JsonProperty("PAY_6") Integer pay6,
        @JsonProperty("BILL_AMT1") BigDecimal billAmt1,
        @JsonProperty("BILL_AMT2") BigDecimal billAmt2,
        @JsonProperty("BILL_AMT3") BigDecimal billAmt3,
        @JsonProperty("BILL_AMT4") BigDecimal billAmt4,
        @JsonProperty("BILL_AMT5") BigDecimal billAmt5,
        @JsonProperty("BILL_AMT6") BigDecimal billAmt6,
        @JsonProperty("PAY_AMT1") BigDecimal payAmt1,
        @JsonProperty("PAY_AMT2") BigDecimal payAmt2,
        @JsonProperty("PAY_AMT3") BigDecimal payAmt3,
        @JsonProperty("PAY_AMT4") BigDecimal payAmt4,
        @JsonProperty("PAY_AMT5") BigDecimal payAmt5,
        @JsonProperty("PAY_AMT6") BigDecimal payAmt6
) {}
