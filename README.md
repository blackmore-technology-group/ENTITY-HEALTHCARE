# ENTITY-HEALTHCARE

**Sealed ENTITY v3.4.0 Healthcare implementation package, evaluated in the current ENTITY v3.4.2 ecosystem.**

**Current canonical core release:** [ENTITY v3.4.2 — Canonical BTDU Release](https://github.com/blackmore-technology-group/ENTITY/releases/tag/v3.4.2).

The sealed domain-package payload in this repository remains the historical v3.4.0 package. Its recorded package-specific requalification against v3.4.1 remains historical evidence; this README does not rewrite that evidence into a new v3.4.2 package qualification. The current v3.4.2 adoption path is open for clean-clone external evaluation.

This repository configures the **one ENTITY Global Passport** for healthcare workflows. It does not define a separate passport protocol and does not modify ENTITY core semantics.

[ENTITY](https://github.com/blackmore-technology-group/ENTITY) · [v3.4.2 release](https://github.com/blackmore-technology-group/ENTITY/releases/tag/v3.4.2) · [ENTITY documentation](https://blackmore-technology-group.github.io/ENTITY-DOCS/) · [Healthcare domain documentation](https://blackmore-technology-group.github.io/ENTITY-DOCS/domains/healthcare.html) · [Domain-package evaluation task](https://github.com/blackmore-technology-group/ENTITY/issues/46)

## What this package is for

Use ENTITY-HEALTHCARE as the starting point when you need a governed passport and provenance layer around healthcare data, records, imaging, derived outputs or other healthcare-domain assets while keeping authority, rights, evidence and custody explicitly separated.

The sealed package includes mappings for **HL7 FHIR** and **DICOM**. Those mappings describe correspondence; ENTITY does not redefine the external standards, and a mapping is not itself a healthcare-regulatory compliance claim.

Typical evaluation paths include:

- attaching persistent provenance and authority context to healthcare-domain assets;
- carrying scoped rights and evidence through derived or exchanged outputs;
- recording custody/provider changes without turning infrastructure possession into sovereign authority;
- testing how a healthcare workflow composes jurisdiction, privacy, trust and technical profiles inside one Global Passport.

## Deploy the package

Required deployment facts:

- `organization`
- `jurisdiction`
- `authority_source`
- `privacy_policy`

`deployment.example.json` is intentionally non-production until every `CONFIGURE-ME` value is replaced with organization-specific facts.

```text
Select package → configure organization facts → connect systems/data → ingest → verify passport → run conformance → deploy
```

## Verify locally

```bash
python tools/verify_package.py
```

The verifier checks repository inventory and the sealed package/source-release binding. A successful package verification does not, by itself, establish a new v3.4.2 qualification claim.

## Sealed package provenance

- Core source: `blackmore-technology-group/ENTITY` PR #41
- Source head: `2d7529fbadb4dd04840d62b751294bf9a7f70ed5`
- Release snapshot: `3ff0e51ca2daabf50bc517e9c6e3438e8c150f1560cca6c99621621e3c855a90`
- Package SHA-256: `b4e901ce37f696fa10666839cb8d3cacbd1fe663070667ca1767a6245e7cf939`

These values describe the sealed historical package payload and should not be rewritten merely because the current core release advances.

## Current evaluation path

- [ENTITY v3.4.2 core release](https://github.com/blackmore-technology-group/ENTITY/releases/tag/v3.4.2)
- [ENTITY documentation portal](https://blackmore-technology-group.github.io/ENTITY-DOCS/)
- [Healthcare domain manual](https://blackmore-technology-group.github.io/ENTITY-DOCS/domains/healthcare.html)
- [Data provenance guide](https://blackmore-technology-group.github.io/ENTITY-DOCS/guides/data-provenance-protocol.html)
- [Standards mapping](https://blackmore-technology-group.github.io/ENTITY-DOCS/developer/standards-mapping.html)
- [Try one current domain-package path from a clean clone](https://github.com/blackmore-technology-group/ENTITY/issues/46)
- [External verification challenge](https://github.com/blackmore-technology-group/ENTITY/issues/55)

## Truth and compliance boundary

External standards remain externally authoritative and are mapped, not redefined. Package verification does **not** establish regulatory compliance, objective external truth, legal title or accounting fair value. Provider custody does not create ENTITY authority.

Deployment-specific privacy, legal, clinical, security and regulatory determinations remain the responsibility of the deploying organization.
