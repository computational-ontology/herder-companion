# Data

| File | Rows | Schema | Status |
|---|---|---|---|
| `ideology_matrix.csv` / `.json` | 12 ideology families | `schemas/ideology_matrix.schema.json` | exploratory (single-coder first pass) |
| `genealogy_edges.csv` / `.json` | 22 edges | `schemas/genealogy_edges.schema.json` | seed |
| `samples/fused_record.example.json` | 1 | `schemas/fused_record.schema.json` | illustrative only |

## Data dictionary — `ideology_matrix`

| Column | Meaning |
|---|---|
| `id` | Stable integer id of the ideology family |
| `family` | Family / current (Spanish label, as coded) |
| `origin_century` | Approximate century of origin |
| `domain_of_gravity` | Romero domain where the ideology's hard core lives (Biológico / Económico / Político / Cultural) |
| `domains_colonised` | Other domains it colonises (`;`-separated in CSV, array in JSON) |
| `a_core` | The hard core defended against the friction of the real (Romero) |
| `dominant_form` | Inclusive / exclusive / ambivalent form of the register it produces |
| `inscription_medium` | Medium of inscription and diffusion (print, mass media, digital…) |
| `SQ1…SQ5` | The five sub-questions of the guiding question *How does each ideology treat the register?* |
| `ccp_domains`, `ccp_variable_families`, `ccp_expected_signal` | Expected footprint in Constitute / Comparative Constitutions Project variables and its direction |
| `coding_status` | exploratory · conclusion · blocked (by α band) |
| `alpha` | Krippendorff's α for the row, once double-coded (empty until then) |
| `codebook_version` | Codebook version the row was coded under |

Identifiers for constitutional units follow Constitute (`constitute_id`, article, clause) and, where available, the CCP `systid`, so tables join to those datasets without translation.

Everything in this folder is *saber* — amendable knowledge — never a claim about what is.
