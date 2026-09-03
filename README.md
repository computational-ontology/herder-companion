# herder-companion — the open companion of *La Constitución en la era digital*

Data, codebook, schemas and (later) notebooks behind the book *La Constitución en la era digital* (manuscript in draft, intended for Herder, Ópera Académica; not yet submitted), the Matrix output of the Computational Ontology project. Documentation is served at **data.ontology360.it** (`docs/`); the matrix site is **ontology360.it**.

Continuation of `ideology-ontology` (CPSS 2026 companion): the ideology × domain × register matrix is the same *saber* layer, versioned forward.

## Layout

```
codebook/   CODEBOOK.md — coding scheme, α policy, re-inscription rule
data/       ideology_matrix.{csv,json} · genealogy_edges.{csv,json} · samples/ · README.md (data dictionary)
schemas/    JSON Schema 2020-12: ideology_matrix · genealogy_edges · fused_record
notebooks/  reproducible analyses (to come): matrix → CCP families → diffusion → endurance
tests/      validate.py — every data file against its schema; normative firewall
docs/       data.ontology360.it (static, no build)
```

## Rules the repository enforces

- **Two-tier use.** Exploratory use is open to anyone. A canonical reading requires two trained coders and an α pass (≥ 0.80 conclusion-grade; 0.67–0.80 exploratory; < 0.67 blocked). Unvalidated readings must not be presented as canonical.
- **Normative firewall.** No record may carry a normative claim: the `normative_claims` field is the sentinel `forbidden_here`, and CI fails otherwise. What ought to follow is the author's, marked, in the text.
- **Re-inscription rule.** A constitutional change counts as a change of meaning only if it alters who may inscribe, what is inscribed, who controls the register, or the temporal scope.
- **One fused record per unit.** Mapping decisions, interpretive revisions as dated events with reasons, and the audit trail, in one object (`schemas/fused_record.schema.json`).

## Status

`0.1.0-exploratory` — single-coder first pass of the matrix exported from the working spreadsheet. Not yet released; no DOI. First frozen release will be deposited on Zenodo under a concept DOI.

## Licence

Data, codebook and documentation: CC BY 4.0. Code (`tests/`, `notebooks/`): Apache 2.0. Attribution required.

Maintainer: Luis Bourguet · LabOnt — Centre for Ontology, Università degli Studi di Torino · ORCID 0000-0002-4673-4486
