# Evidence for Chapter 9

Recorded on 16 November 2026 against https://optiroute-ai-phi.vercel.app.

These are observations of an HTTP interface and its returned routing decisions.
They do not establish generated-answer accuracy, measured savings, inference
latency, actual local execution, or end-to-end privacy enforcement.

## Files

- `api_checks.json`: 16 exact request bodies, UTC timestamps, status codes,
  complete parsed responses, and hashes of the original response bytes.
- `summary.json`: derived counts, selected model names, and validation details.
- `reproduce_checks.py`: standard-library Python client; no packages required.
- `analyse_checks.py`: recomputes the reported counts from the saved JSON.

## Check the recorded findings

Run from this directory using Python 3:

```powershell
python analyse_checks.py
```

Recorded outcomes:

| Quantity | Result |
|---|---|
| Recorded requests | 16 |
| Expected HTTP statuses matched | 16 of 16 |
| Registry entries | 8 distinct model names |
| Configured sensitive-query approved entries | 2 |
| Valid routing responses selecting a registry entry | 4 of 4 |
| Invalid requests rejected with structured HTTP 422 details | 9 of 9 |
| Privacy-constrained selections in the approved set | 2 of 2 |
| Explicit keyword example classified as sensitive | 1 of 1 |

The two privacy selections are a subset of the four routing requests. Do not add
these rows together. The remaining requests are the model-registry and privacy
configuration GET requests. Each request was executed once, sequentially.

## Repeat the live experiment

First preserve a copy of this evidence directory: the following command replaces
`api_checks.json` with observations from the new run.

```powershell
python reproduce_checks.py
python analyse_checks.py
```

The recorded response file has SHA-256:

```text
d85201326b0520e3ac157884795d6a0f345a3eb701035df514b322bf28f2da29
```

The per-response hashes are for original HTTP response bytes, before JSON
reformatting. They are provenance records, not signatures issued by the server.
The complete original JSON response bodies are retained as parsed JSON values.

## How to explain these results in a defence

The experiment exercised selected input constraints and policy configurations.
All nine deliberately invalid requests were rejected with HTTP 422 and structured
field-level errors. The four valid routing requests selected registered models.
The two requests constrained by Private mode or explicit sensitivity selected a
model from the current approved set. This supports the reported behavior for
those inputs; it is not an estimate of general accuracy or reliability.

The ordinary query was `Explain binary search.` The artificial sensitive query
was `This is confidential proprietary information.` No real personal data was
submitted. The explicit sensitivity flag and keyword were both present in the
sensitive routing request, so their individual causal contributions cannot be
separated by this experiment. The standalone sensitivity request confirms only
that the keyword rule fired for the supplied artificial sentence.

The HTTP API returned prediction, cost, and latency fields too. Those fields are
preserved in the raw evidence for completeness, but are not used as verified
performance results in the report. No generated answer was scored. No provider
execution or internal network traffic was independently observed.

The deployed server's build identifier was unavailable. Inputs were deliberately
selected rather than randomly sampled, and there were no repeated trials or
load tests. Later runs may differ if the server or configuration changes. The
archived evidence supports the dated observations, not a permanent guarantee.
