# Public-example benchmark

Evaluated 25 public solved examples using the same predictor as the full run. These examples informed development; this is not a held-out evaluation or a hidden-test score.

| Check | Matches | Rate |
| --- | ---: | ---: |
| amount_safe_to_pay | 2/25 | 8% |
| affordability_status | 22/25 | 88% |
| recommended_payment_method | 24/25 | 96% |
| payment_plan | 23/25 | 92% |
| earliest_date_for_full_payment | 19/25 | 76% |
| spending_changes_needed | 21/25 | 84% |
| Semantic payment schedule | 23/25 | 92% |

Mean absolute safe-amount error, normalized by each requested amount: **5.20971030%** (baseline **5.21125645%**). Amounts span multiple currencies, so raw currency errors are not averaged together.

The only retained forecast change is half-up cent rounding of historical means. Six other tested variants had no benefit or regressed. Categorical counts remain unchanged. See `improvement_report.md` for the full classification of all 23 amount misses, categorical review and unresolved zero-capacity cases.

The 31-test suite covers the original forecast, evidence, plan and validator cases plus five packaging guards. Full-run results and hash checks are recorded in `validation_report.json`. Validation proves feasibility under the documented forecast, not agreement with hidden labels or a statistical worst-case spending bound.

```bash
python3 code/main.py --samples
python3 code/analyze_samples.py --summary-only
python3 -m unittest discover -s code/tests -v
python3 code/package_submission.py --refresh
```
