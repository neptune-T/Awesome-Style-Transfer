# Survey catalogue and evidence — v26

This directory accompanies *Style Transfer: A Decade Survey*. It records 136
included publications (108 core, 24 adjacent, 4 boundary) from 301 unique
bibliographic records. `catalogue.csv` records paper IDs, source links, carrier
labels, output modalities and configuration notes.

## Selection and units

`evidence_selection.csv` lists every included paper, plus the contextual TokenFlow
source outside the included corpus, and membership in the fixed
source-local extraction sample: 39 studies, comprising 38 core and TokenFlow as
correspondence machinery. Reuse, binding and consistency investigations
overlap. The consistency denominator uses 16 core studies; TokenFlow is contextual.
The 192 evidence rows are observations, not independent studies. Seven
`not_verified` observations record unestablished properties and do not count as
measured evidence. Extraction and coding were AI-assisted; original review and
verification fields are retained.

Eligibility descriptions summarize the recorded investigations, rather than a
preregistered sampling plan. Papers outside the extraction set are not assumed to
lack a test. A3GS, Styl3R and ZDySS are new catalogue/source checks; their admission
does not alter the fixed protocol frequencies. Further source checks are provided
as `additional_*_observations.csv`, separately from that sample.

## Data files

| File | Content |
|---|---|
| `evidence_register.csv` | Record IDs, source links, page/figure/table, intervention, outcome, interpretation, confounders, evidence type and review status |
| `source_manifest.csv` | Pinned source versions, PDF links and hashes |
| `evidence_selection.csv` | Catalogue-to-sample crosswalk, including entries outside the fixed sample |
| `protocol_reuse.csv` | 28 studies; excluding two exemplar-statistic-only methods leaves 26 acquired-state cases |
| `protocol_binding.csv` | 20 studies; direct leakage means reference-only semantic copying, rather than general embedding similarity |
| `protocol_consistency.csv` | 16 core studies; quantitative reappearance is distinct from masked visible-flow agreement |
| `claims.csv`, `claim_support.csv` | Sample-bounded claims, study/author-cluster support and counterexamples |
| `survey_comparison_sources.csv` | Cell-level source locations behind the survey-comparison marks |
| `benchmark_*.csv` | Resource catalogue, protocol units and source observations |
| `figure_provenance.csv` | Figure origins, versions, licenses and adaptations |
| `catalogue_additions.csv` | Three new primary-source checks, PDF hashes and configuration rationale |

`records` fields join to `record_id`; `cite_key` joins to the manifest/catalogue.
Empty or unclear fields represent missing source information. `no` records a test
not identified in the inspected source, rather than an impossibility. Run
`python verify_counts.py` here to check counts, identifiers, source anchors, joins
and file hashes. No underlying baseline/model experiments are run.

The repository license does not replace third-party figure licenses. Source
credits are centralized in `figure_provenance.csv` and the supplementary credits.
