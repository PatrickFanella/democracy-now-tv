# Shared engine release

This repository owns the original frontend and its branding. The optional shared
viewer package and the headless core are separate release lanes. Core 0.1.2 is
pinned in `deploy/archive-core.env` and `deploy/core-release.json`; changing those
pins does not require a frontend dependency update or rebuild.

Run `make verify` before release. Check the engine's registry digest and source
labels against the receipt. Retain the previous engine, frontend, configuration,
and a fresh independent database checkpoint. Apply the engine's additive
migrations with an operator role and use a SELECT-only role for public serving.
Qualify catalog, on-demand playback, shared-channel timing, and cross-collection
denial through the original frontend before changing the production API service.

Democracy Now! remains source-streaming only; this release does not enable local
acquisition, caching, or transcoding for that collection. Bill Nye keeps the
already verified local originals and their original dates and source credits.
A template's configured collection must match the API scope and its `site.json`.

Upgrades use a reviewed PR carrying an immutable digest, compatible API/module
versions, and unchanged checksums for previously applied migrations. Restore the
previous checkpoint in an isolated environment before claiming database rollback;
preserve newer production writes before selecting any earlier snapshot.

Public deployment follows the separate recorded owner decision. Publishing a
release or merging a pin is separate from changing the live API.
