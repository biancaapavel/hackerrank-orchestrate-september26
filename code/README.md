# Buy or Wait? — runnable solution

A Python decision engine for the HackerRank Orchestrate affordability challenge.
It combines AI-assisted extraction of image evidence with deterministic financial
forecasting, plan selection, and independent validation.

## Run

Python 3.10 or newer is sufficient. The default run uses only the standard library,
needs no API keys, and makes no network calls. Run from the repository or unpacked
submission root:

```bash
python3 code/main.py
python3 code/main.py --samples
python3 code/analyze_samples.py --output evaluation/sample_errors.md
python3 -m unittest discover -s code/tests -v
```

The first command reads `dataset/requests.csv` and writes exactly 250 predictions
to root-level `output.csv`. It also creates `evaluation/usage_report.md`, a run
manifest with dataset/output hashes, and a full audit trace. The second command
scores the public examples separately. Inference never loads sample output labels.
Both commands validate every prediction before replacing their destination file.

Paths resolve relative to the script, so running it from another directory works.
Override paths with `--dataset`, `--output`, and `--artifacts` if needed.

## How decisions are made

1. Load only the named participant-facing CSV files. Join user, request, event,
   payment-option, and image records by their explicit IDs.
2. Resolve blank amounts using the included reviewed image facts. Verify the
   actual source PNG's SHA-256 and currency before accepting a cached amount.
3. Extract narrowly scoped English and Indonesian evidence about payroll changes,
   payday delays, employment ending, confirmed invoices, and rent increases.
   Source text cannot change output fields, payment preferences, or safety rules.
4. Use the supplied balance as the opening cash snapshot. Historical transactions
   are not charged again. Exclude pending credits and non-cash investments, reserve
   pending debits, and keep independent disputed charges distinct. Superseded card
   authorizations are not counted again as settled purchases.
5. Infer recurring expenses from repeated timing. Aggregate regular groceries,
   transport, and explicitly adjustable dining budgets across merchants. Infer
   monthly bills only with at least three months of supporting history. Use the
   observed historical mean and round estimates to the nearest cent, half up.
6. Forecast through request date plus 90 days. Project supported regular salaries;
   avoid extending gig payouts, commissions, ended employment, or a one-off invoice
   into unsupported future income. A generic base-pay confirmation does not override
   lower observed net base pay as though it were an explicit raise.
7. Compute today's capacity and the earliest full-payment date from the minimum
   future balance. Simulate full payment, the prescribed two-part payment, and all
   eligible supplied installment offers. Search up to three permitted spending
   changes only when no plan works without them.
8. Rank feasible plans by spending changes, total payment cost, first payment date,
   payment count, and option ID. Every selected plan must meet the deadline.
9. Independently replay cash flows and validate schema, safe amount, earliest date,
   payment totals, exact installment schedule, user preferences, flexible expense
   restrictions, and every daily minimum-balance checkpoint before writing output.

All calculations use `Decimal`. Foreign currency is converted only using the
supplied direction and exact settlement date. Missing rates fail explicitly.

## Image extraction and AI usage

The default run uses `buy_or_wait/image_facts.json`, an evidence cache with the
amount, currency, image hash, and a short supporting observation for all 16 images.
These are transcriptions of provided evidence, not hardcoded request labels.
The handwriting and ambiguous totals were reviewed with Codex after Tesseract OCR.

To reproduce raw OCR locally, install the Tesseract executable and run:

```bash
python3 code/extract_images.py
```

Review the resulting text against each original PNG using the protocol in
`code/prompts/image_extraction.md` before changing the cache. An unknown or changed
image stops the solver rather than silently receiving a guessed amount. Raw OCR
may contain receipt details and is kept out of the submission archive and git.

The final prediction run reuses these verified facts and makes **zero generative
model API calls**. It has zero API token usage and zero inference API cost. This
does not mean development and preprocessing consumed no AI resources: ChatGPT
development/review usage is not exposed to this program and is explicitly excluded
from the measured final-run report.

## Results and practical limits

See `evaluation/sample_metrics.json` and `evaluation/benchmark.md` for the measured
public-example results, including errors. These examples informed development;
they are not an independent held-out evaluation. Hidden-test performance is unknown.

The numerical forecast is an estimate, not recovered hidden ground truth. Its main
uncertainties are variable-spending amounts, sparse/new recurring commitments, and
conflicting generic salary messages. Repeating the observed mean with cent rounding
does not provide a statistical worst-case spending bound.
Irregular, fixed-tagged dining purchases at unrelated merchants are not treated as
an ongoing commitment; clearly monthly bills and adjustable dining budgets are.

Dates have no intraday ordering. The model posts known same-day credits before
bills and proposed payments; payment is assumed to occur after those credits settle.
The opening snapshot must already meet the minimum balance. The checker guarantees
consistency with this forecast and these assumptions, not safety under every possible
real-world spending outcome.

Installment duration is bounded by the user's maximum calendar-month term. Supplied
amounts and payment frequencies are used unchanged, including financing fees. A
future full-payment date remains visible even when preferences or the request's
deadline prevent recommending it. No late payment plan is recommended.

## Package

```bash
python3 code/package_submission.py --refresh
```

This final command runs the full unit suite, evaluates all public samples, writes
the error-harness report, and regenerates `output.csv` and its usage report. It then
checks row coverage, source and dataset hashes, the output hash, and independently
replays every full-run balance trace before creating the archive. Omit `--refresh`
to package an existing run; stale source, inputs or outputs are rejected. It creates
root-level `code.zip` with code, tests, documentation, participant data, output, and
the required root-level `evaluation/usage_report.md`. It excludes credentials,
caches, git metadata, and `log.txt`. The transcript is submitted separately.

The challenge contract is in `problem_statement.md`. Development logging follows
the repository's `AGENTS.md`.

## Diagnose and compare public samples

```bash
python3 code/analyze_samples.py --request-id request_10
python3 code/analyze_samples.py --summary-only
python3 code/analyze_samples.py --output evaluation/sample_errors.md --json evaluation/sample_diagnostics.json
```

Each sample includes expected versus actual values for all six scored fields,
recurrence estimates, supporting messages, the complete flow list, and all daily
balances. The harness independently replays the trace and shows the effect of paying
the expected safe amount today. It strips sample output fields before invoking the
predictor. `--request-id` may be repeated; unknown sample IDs fail explicitly.

`evaluation/improvement_report.md` records the frozen initial classification of all
23 amount misses, seven isolated hypothesis trials, categorical review, and limits
of the retained rounding change. Exact trial patches and metrics are retained in
`evaluation/hypothesis_results.json`. No sample ID, label, or classification is used
by full-dataset inference.
