# Public-example benchmark

Evaluated 25 public solved examples using the same predictor as the full run.
These examples informed development. This is a development benchmark, not an
independent holdout or a measure of hidden-test performance.

| Check | Matches | Rate |
| --- | ---: | ---: |
| Affordability status | 22/25 | 88% |
| Recommended payment method | 24/25 | 96% |
| Payment schedule (dates and numeric amounts) | 23/25 | 92% |
| Earliest full-payment date | 19/25 | 76% |
| Spending changes (exact text) | 21/25 | 84% |
| Safe amount (exact to the cent) | 2/25 | 8% |

Mean absolute safe-amount error, normalized by each request's requested amount:
**5.21%**.
This is not 1 minus an overall hackathon score. Amounts span five currencies, so
we do not average unconverted absolute currency errors across users.

All 25 sample rows and 250 evaluation predictions pass the independent contract
and balance-replay validator. The 26 unit tests cover cash-flow troughs, date-90
obligations, pending credits/debits, investment cash states, invoice recurrence,
image-payday ambiguity, multilingual facts, untrusted instructions, FX date/direction,
preferences, deadlines, exact plans, protected expenses, and rejection of tampering.

`sample_metrics.json` contains every mismatch. Money formatting is normalized only
for the semantic payment-schedule metric; the exact-field metrics are literal.

The dominant remaining uncertainty is recurrence/variable-spending estimation.
The supplied data does not expose the hidden forecast model. This solution uses
historical means with upward cent rounding, documented cadence inference, and
conservative income recognition. Validation proves feasibility under the documented
forecast, not equality to hidden financial labels.

Reproduce:

```bash
python3 code/main.py --samples
python3 -m unittest discover -s code/tests -v
```
