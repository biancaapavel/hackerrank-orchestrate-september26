# Token usage and cost — final full-dataset run

Generated: 2026-09-12T15:12:04.466602+00:00. Requests: **250**.
Output SHA-256: `0f35602bdfd16fbe563d4d40b5a459171b329f13fdca4f63176cd2f0f3998904`.
Runtime: 0.683 seconds. All predictions passed validation.

| Provider / model | Calls in final run | Input tokens | Output tokens | API cost (USD) |
| --- | ---: | ---: | ---: | ---: |
| Generative model providers: none invoked | 0 | 0 | 0 | 0.00 |
| Tesseract OCR / Codex-reviewed image facts (cached preprocessing) | 0 | 0 | 0 | 0.00 |
| **Total** | **0** | **0** | **0** | **0.00** |

- Total tokens: **0**; average tokens per request: **0**.
- Estimated total inference API cost: **USD 0.00**.
- Estimated average inference API cost per request: **USD 0.00**.
- Verified cached image facts: **16**. No fresh OCR/model calls occurred in this run.

The measured run uses the Python standard library and previously extracted image
facts, verified against the source PNG hashes. There are no hosted model calls,
API credentials, or live external financial data. Local compute cost is not priced.

During development, Tesseract OCR processed the 16 supplied images and Codex in
ChatGPT Work (OpenAI) assisted with image review, code, and evaluation. The exact
development model identity, model-call count, tokens, and cost are not exposed to
the runnable program and are **not measured**, rather than claimed to be zero.
They are outside the final prediction run summarized above. The image facts cache
and extraction protocol are included so that this distinction is reviewable.

This report is regenerated only by the full-dataset run. Running public-example
evaluation does not overwrite it. `run_manifest.json` records input and output
hashes connecting these measurements to the delivered predictions.
