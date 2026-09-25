# ENTITY-HEALTHCARE

**ENTITY v3.4.0 executable Healthcare implementation package.**

This repository configures the **one ENTITY Global Passport** for healthcare workflows. It does not define a separate passport protocol and does not modify ENTITY core semantics.

[ENTITY](https://github.com/blackmore-technology-group/ENTITY) · [v3.4.0 release](https://github.com/blackmore-technology-group/ENTITY/releases/tag/v3.4.0) · [Global Passport documentation](https://github.com/blackmore-technology-group/ENTITY/blob/main/docs/v3.4/GLOBAL_PASSPORT.md) · [Domain packages](https://github.com/blackmore-technology-group/ENTITY/blob/main/docs/v3.4/DOMAIN_PACKAGES.md)

## What this package is for

Use ENTITY-HEALTHCARE as the starting point when you need a governed passport and provenance layer around healthcare data, records, imaging, derived outputs or other healthcare-domain assets while keeping authority, rights, evidence and custody explicitly separated.

The package includes mappings for healthcare standards identified by the v3.4 release, including **HL7 FHIR** and **DICOM**. Those mappings describe correspondence; ENTITY does not redefine the external standards.

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

The intended v3.4 deployment flow is:

```text
Select package → configure organization facts → connect systems/data → ingest → verify passport → run conformance → deploy
```

## Verify locally

```bash
python tools/verify_package.py
```

The verifier checks the repository inventory and the package/source-release binding.

## Release binding

- Core source: `blackmore-technology-group/ENTITY` PR #41
- Source head: `2d7529fbadb4dd04840d62b751294bf9a7f70ed5`
- Release snapshot: `3ff0e51ca2daabf50bc517e9c6e3438e8c150f1560cca6c99621621e3c855a90`
- Package SHA-256: `b4e901ce37f696fa10666839cb8d3cacbd1fe663070667ca1767a6245e7cf939`

## Go deeper

- [ENTITY v3.4.0](https://github.com/blackmore-technology-group/ENTITY/releases/tag/v3.4.0)
- [Developer portal](https://github.com/blackmore-technology-group/ENTITY/blob/main/DEVELOPERS.md)
- [Engineering evidence](https://github.com/blackmore-technology-group/ENTITY/blob/main/docs/ENGINEERING_EVIDENCE.md)
- [Open contributor tasks](https://github.com/blackmore-technology-group/ENTITY/issues?q=is%3Aissue+is%3Aopen)

## Truth and compliance boundary

External standards remain externally authoritative and are mapped, not redefined. Package verification does **not** establish regulatory compliance, objective external truth, legal title or accounting fair value. Provider custody does not create ENTITY authority.

Deployment-specific privacy, legal, clinical, security and regulatory determinations remain the responsibility of the deploying organization.
