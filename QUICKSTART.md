# ENTITY healthcare Implementation Package

This package configures the one ENTITY Global Passport; it does not define a separate passport.

1. Copy `deployment.example.json` and replace every `CONFIGURE-ME` value.
2. Validate organization authority, jurisdiction and package-specific policy inputs.
3. Use `EntityGlobalPassportSDK.package_plan()` to resolve the executable profile stack.
4. Connect the source system and use `ingest_package_file()` for continuous provenance.
5. Verify the resulting Global Passport and run the package conformance vectors.

External standards are mappings only. ENTITY does not redefine them, and package validation does not establish regulatory compliance.
