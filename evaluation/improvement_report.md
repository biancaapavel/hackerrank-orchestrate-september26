# Improvement report â€” Buy or Wait?

## Result

The diagnostic harness and submission checks are implemented. All 23 original safe-amount misses were classified before changing forecast logic. Seven isolated forecast hypotheses were tested against all 25 public examples and the complete existing 26-test suite. Only half-up rounding was retained. The final suite also contains five new packaging tests.

Mean absolute safe-amount error, divided by each requested amount, changes from **5.21125645%** to **5.20971030%**. This is only **0.001546 percentage points**. Every categorical count is unchanged. There is no material accuracy breakthrough, and the two zero-capacity discrepancies remain unresolved.

These 25 public samples are development data. No hidden labels were accessed. No request-specific rule, fitted income, or spending adjustment was introduced. Further amount tuning stopped after the bounded comparisons failed to produce a meaningful gain, within the proposed 15-hour ceiling.

| Field | Before | After |
| --- | ---: | ---: |
| amount_safe_to_pay | 2/25 | 2/25 |
| affordability_status | 22/25 | 22/25 |
| recommended_payment_method | 24/25 | 24/25 |
| payment_plan | 23/25 | 23/25 |
| earliest_date_for_full_payment | 19/25 | 19/25 |
| spending_changes_needed | 21/25 | 21/25 |

## What changed

- `code/analyze_samples.py`: all six expected/actual fields, source recurrence history and messages, every trace flow, and all daily balances. It independently replays baseline and planned balances, and shows the counterfactual of paying the sample's expected safe amount today. Labels are stripped before the predictor is invoked.
- `forecast.py`: use `ROUND_HALF_UP` when rounding historical means to cents. The inference categories, calendar, horizon and income policy stay as evaluated in the baseline.
- `package_submission.py --refresh`: run the full unit suite, sample evaluation, the diagnostic harness and full inference, then verify source/data/output hashes, complete row coverage, usage-report identity and all full-run balance traces. Publish the ZIP atomically after validation.
- `main.py`: record source hashes alongside dataset and output hashes in the full-run manifest.
- Five packaging regression tests reject changed code, changed inputs, altered output and missing predictions, and verify that a matching run succeeds.

## Frozen initial error classification

Confidence describes the visible-data diagnosis, not certainty about the hidden forecast. No amount discrepancy is uniquely explained by changing income at its initial trough. The two boundary cases have a confirmed simulated cash deficit but an unknown reason for the positive sample labels.

| Bucket | Cases |
| --- | ---: |
| Amount / timing estimate | 14 |
| Recurring-expense inference | 4 |
| Boundary / cash deficit | 2 |
| Unresolved from visible data | 3 |

| Sample | Expected safe | Baseline safe | Trough day | Primary bucket |
| --- | ---: | ---: | ---: | --- |
| request_02 | 17229139.2 | 18336765.46 | 8 | Amount / timing estimate |
| request_03 | 873000 | 1121649.64 | 11 | Recurring-expense inference |
| request_04 | 8401800 | 12357921.12 | 9 | Recurring-expense inference |
| request_05 | 737 | 0 | 90 | Boundary / cash deficit |
| request_06 | 603.3 | 615.57 | 10 | Amount / timing estimate |
| request_07 | 87170.56 | 86237.19 | 15 | Amount / timing estimate |
| request_08 | 284.57 | 285.18 | 6 | Amount / timing estimate |
| request_09 | 166.61 | 151.86 | 90 | Unresolved from visible data |
| request_10 | 12700 | 0 | 90 | Boundary / cash deficit |
| request_11 | 12510645 | 12319866.6 | 11 | Amount / timing estimate |
| request_12 | 65164 | 60370.2 | 87 | Unresolved from visible data |
| request_13 | 433.4 | 812.01 | 68 | Recurring-expense inference |
| request_14 | 597.74 | 616.27 | 10 | Amount / timing estimate |
| request_15 | 83.05 | 5.07 | 8 | Amount / timing estimate |
| request_17 | 243849.58 | 243023.67 | 13 | Amount / timing estimate |
| request_18 | 462 | 546.02 | 7 | Amount / timing estimate |
| request_19 | 28820 | 25176.12 | 10 | Amount / timing estimate |
| request_20 | 5400 | 8969.66 | 6 | Amount / timing estimate |
| request_21 | 1543.35 | 1574.4 | 9 | Unresolved from visible data |
| request_22 | 475.46 | 480.66 | 9 | Amount / timing estimate |
| request_23 | 9152 | 8360.16 | 7 | Amount / timing estimate |
| request_24 | 13420 | 13539.25 | 9 | Amount / timing estimate |
| request_25 | 1425000 | 2445438.16 | 8 | Recurring-expense inference |

### Per-sample findings

- **request_02** (medium): The first trough precedes the documented raise. Groceries, transport, utilities and healthcare means determine the reserve; the excluded 21-day dining stream next occurs after that trough. No wrong income explains today's error.
- **request_03** (medium): Nine fixed-tagged dining purchases occur every 21 days; the blanket fixed-dining exclusion omits a due purchase on the first trough date. Including this budget is a hypothesis, not a full explanation of the residual.
- **request_04** (medium): Thirteen fixed-tagged dining purchases occur every 14 days, including a projected purchase before payday. They are excluded solely by flexibility. One omitted mean purchase explains part, but not all, of the large error.
- **request_05** (high on trace; unknown label cause): No salary is projected after Final employer payroll. Baseline first breaches the floor on day 88 with rent; day-90 transport only worsens it. No explicit or duplicate flow exists. Dropping the final day cannot recover the positive label.
- **request_06** (medium): The trough precedes temporary salary. Variable groceries, transport, shopping and utilities estimates explain a small reserve discrepancy. Fixed dining is also excluded, but adding two pre-payday dining purchases would overshoot the label.
- **request_07** (medium): The documented salary delay is respected. Variable groceries, transport, dining and utility estimates set the pre-payday trough; rounding alone cannot explain INR 933.37.
- **request_08** (medium): The EUR 0.61 amount miss is at the first pre-salary trough. The later-date/status error is distinct: long-run expenses consume the extra income by the last forecast days. The reduced-pay message conflicts with historical amounts, so salary recovery must not be invented.
- **request_09** (low): No eligible confirmed salary. Small variable reserve differences accumulate over 90 days and determine whether the request clears the floor. The final-day rent is real; removing it would conceal the uncertainty. A positive label is not proof of forecast safety.
- **request_10** (high on trace; unknown label cause): Unconfirmed gig earnings are correctly excluded. Baseline first breaches the floor on day 87 with rent, before day-90 groceries. No duplicate or explicit flow exists. The positive label requires an unsupported change to income, expenses or horizon.
- **request_11** (medium): The amount trough is before the first salary; variable reserves explain its difference. Lower settled base salary is used instead of the larger generic confirmation. The extra cloud stop may arise from a marginal reserve error; earliest-date disagreement also depends on later cadence/income.
- **request_12** (low): The ended seasonal contract correctly contributes no income. Variable dining, shopping, utilities and essential budgets accumulate at the day-87 trough. No duplicate or final-day charge is present. No unique amount-estimation rule is recoverable from the label.
- **request_13** (medium): Thirteen fixed-tagged dining purchases repeat every 14 days but are omitted. Several fall before the day-68 trough. The second household income is irregular and no longer observed; its omission is supported, so do not invent it to fit the label.
- **request_14** (medium): Resumed salary is explicitly confirmed and begins after the first trough. Variable groceries, transport, utilities, shopping and healthcare amounts set the EUR 18.53 difference.
- **request_15** (medium): The first salary is correctly dated after the trough. The request-day groceries prediction and the second weekly groceries/transport events before payday create timing sensitivity; the EUR 77.98 gap is too large to attribute to cent rounding.
- **request_17** (medium): Confirmed salary is correct. The first trough reflects two groceries/transport periods plus dining and utilities. The earliest-date miss involves later recurring expense totals as well as the small initial amount error.
- **request_18** (medium): Dining next falls on payday, so the same-day closing convention keeps it out of the preceding trough. The EUR 84.02 gap is near one dining reserve, but the visible dates do not justify moving it earlier.
- **request_19** (medium): Weekly groceries are due on request day and again before payday. A separate image-backed grocery purchase settled the day before and is already in opening cash. Mean amounts/cadence affect the gap; no duplicate future charge is present.
- **request_20** (medium): The pending refund is excluded and the pending order and image-backed telecom debit are reserved separately. The gap is near a dining period, whose observed 21-day cadence next falls after payday; its date cannot be shifted solely to fit the label.
- **request_21** (low): Uncapped baseline capacity is USD 1673.12 versus a 1543.35 label. Dining and transport next occur after payday; moving one of each before payday would nearly bridge the gap but lacks date evidence. This timing uncertainty causes the status/change mismatch.
- **request_22** (medium): Unrealized portfolio value is excluded. A small variable-reserve error sets today's difference. Fixed dining is omitted, but adding its next pre-payday mean would overshoot the label; test the rule across all samples.
- **request_23** (medium): Pending prize credit is excluded and the pharmacy debit is reserved. Two groceries periods fall before salary. Variable mean and cadence assumptions explain the remaining uncertainty.
- **request_24** (medium): Settled prize proceeds are already in opening cash and not repeated. The scheduled insurance debit is a distinct obligation. The small gap lies in variable recurring amounts before payday.
- **request_25** (medium): Twenty-five fixed-tagged dining purchases repeat every seven days. Two projected purchases before payday are excluded. The error is near one mean dining amount; test inclusion globally because it may overreserve two occurrences.

## Isolated hypothesis results

Every row below used the same public requests and full original 26-test suite. Each variant changed only its stated forecast assumption in a separate copy. The four-month policy fails existing tests that require a supported three-month commitment to be forecast. The retained code subsequently passes all 31 tests.

| Hypothesis | Mean normalized error | Status | Method | Schedule | Earliest date | Changes | Tests | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Baseline | 5.21125645% | 22 | 24 | 23 | 19 | 21 | 26 passed | Reference |
| half_up | 5.20971030% | 22 | 24 | 23 | 19 | 21 | 26 passed | retained |
| history_2_months | 5.21125645% | 22 | 24 | 23 | 19 | 21 | 26 passed | rejected |
| history_4_months | 5.21125645% | 22 | 24 | 23 | 19 | 21 | Failed | rejected |
| median_amounts | 5.76094860% | 22 | 23 | 22 | 21 | 20 | 26 passed | rejected |
| include_fixed_dining | 6.56178943% | 20 | 22 | 21 | 18 | 20 | 26 passed | rejected |
| recent_90_day_mean | 5.35870089% | 21 | 23 | 22 | 19 | 21 | 26 passed | rejected |
| 20_percent_trimmed_mean | 5.35908604% | 22 | 23 | 22 | 19 | 20 | 26 passed | rejected |

Exact code patches, original source hashes, test output and all per-sample metrics are stored in `hypothesis_results.json`. `baseline_metrics.json` and `initial_error_classification.json` preserve the pre-change evidence.

## The two zero-capacity cases

Both were traced from the opening balance through the first minimum-balance breach. All projected obligations in these cases come from recurring expense streams; there is no explicit-event copy or repeated event/date pair to remove.

| Sample | First breach | Trigger | Headroom at breach | Headroom at day 90 | Headroom if day 90 alone is excluded |
| --- | --- | --- | ---: | ---: | ---: |
| request_05 (ZAR) | Day 88, 2026-02-02 | Rent 4,972 | -3,803.33 | -4,939.39 | -4,525.04 |
| request_10 (INR) | Day 87, 2025-03-03 | Rent 69,100 | -36,573.43 | -47,349.51 | -36,573.43 |

Excluding only the terminal day leaves both amounts at zero. Employment has ended in request_05; request_10's gig payout is unconfirmed. Adding income, omitting rent, or shortening the horizon sufficiently to recover the labels is not supported. The day-90 safety check is retained.

## Categorical review

| Sample | Finding and action |
| --- | --- |
| request_08 | The first amount miss is only EUR 0.61, but baseline capacity after the expected 2025-04-15 payment date is limited to EUR 760.16 by later expenses, below the EUR 996.60 request. The reduced-pay message names the same amount as older regular salary; it does not justify inventing a further raise. Keep the validated spending-change plan. |
| request_09 | Paying EUR 166.61 would exceed baseline 90-day headroom by EUR 14.75. The final-day rent is a supported obligation. The amount estimators tested did not yield a globally acceptable repair; retain the fallback. |
| request_11 | The prescribed dining reduction saves IDR 684,072.55 under the baseline, less than its IDR 790,133.40 initial payment shortfall. The extra cloud stop is required by that forecast. Mean/median alternatives were tested globally; do not delete a necessary action to match the label. |
| request_12 | The seasonal contract has ended. With no supported future income, the baseline requires changes to keep the installment plan above the minimum. A day-90 exclusion has no effect; the trough is day 87. |
| request_17 | Baseline capacity from 2026-03-15 is INR 273,240.60, below the INR 274,600 request by INR 1,359.40. The selected installment offer is already correct; moving the full-payment date requires a justified forecast change. |
| request_19 | The payment-plan mismatch is the direct consequence of the safe-amount miss. The implementation correctly uses the required amount-today plus remainder schedule. |
| request_21 | Baseline uncapped capacity is USD 1,673.12 versus a USD 1,543.35 label. Dining and transport are next due after payday on their observed cadence. Moving them earlier merely to require the labeled changes is unsupported. |

## Reproduce

```bash
python3 code/analyze_samples.py --request-id request_10
python3 code/analyze_samples.py --summary-only
python3 code/package_submission.py --refresh
```

`sample_errors.md` contains the full final diagnostic tables; `sample_diagnostics.json` adds the complete source history for analysis. `sample_metrics.json` records remaining errors. The final full-dataset run is identified by `run_manifest.json` and `usage_report.md`; final validation results are recorded in `validation_report.json`. The runnable archive excludes `log.txt`, which is kept separately for transcript preparation.
