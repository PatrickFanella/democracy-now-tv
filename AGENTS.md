# Standalone video app

This repository owns its frontend, design system and deployment configuration.
VHNESS owns the shared engine and `@subcult/archive-viewer` package. Import the
published package; never copy or edit shared implementation here. The exact
package dependency, pnpm lock, engine digest and release compatibility receipt
must change together through a reviewed upgrade. The former generated viewer
manifest is retained in docs/legacy-viewer-manifest.json for migration provenance.
Existing generated deployment tools remain pinned by docs/engine-tools.json.

Run make verify. Browser rendering, decoding, audiovisual review, shared-channel
timing, independent restore and deployment are separate checks. Runtime data,
media and secrets stay outside Git. Public deployment requires its separate
owner decision. Preserve original dates, source credit and replay labels.
