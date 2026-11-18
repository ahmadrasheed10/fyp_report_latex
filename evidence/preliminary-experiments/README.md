# Supporting evidence for the FYP-I preliminary experiments

Chapter 8 reports observations from existing API records. No new measurements
were generated for the report revision.

The chapter uses seven records from `api_checks.json`, identified in
`chapter9_evidence_index.json`: registry, privacy-config, legacy, balanced,
private, sensitive-balanced, and keyword-positive. The source file also contains
diagnostic requests outside the scope of Chapter 8; they are retained to preserve
the original record. Do not treat the full archive as the chapter's experimental
sample or as a benchmark of answer quality.

The reported evidence comprises eight configured model names, two sensitive-query
approvals, four returned routing selections, and one keyword-screening response.
The selected names and flags in the tables were checked against the saved JSON.

`reproduce_checks.py` is the original collection script. Running it contacts the
live API and overwrites `api_checks.json`, so preserve a copy of this directory
before repeating the requests. The script also runs the additional diagnostic
requests retained in the original archive. Later results can differ because no
server build identifier was supplied. This is not evidence of repeated trials.

The original request settings remain in the raw records for provenance. Numerical
routing-threshold values are intentionally omitted from the report narrative and
tables. No source records have been altered to conceal those settings.

The API's predicted-quality, cost, and latency fields are retained in the source
responses but are not independently verified performance measurements. No answer
accuracy, cost savings, inference speed, or complete privacy guarantee follows
from the observations. The formal test-case and test-metric sections are deferred
to FYP-II.

The current AetherFlow deployment is https://aether-flow-gamma.vercel.app/. The archived response file retains its original collection URL and metadata; it is not a new measurement of the current deployment.
