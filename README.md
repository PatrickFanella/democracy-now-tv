# Democracy Now! broadcast archive

A standalone episode library and shared scheduled replay channel, built on the
shared VHNESS engine. This repository owns its frontend, design system, assets,
and deployment configuration. The viewer adapter and deployment helpers are
pinned generated copies, verified against engine revision `9f6ad5b1fa3f20e2c3f063f30ed98d8d4a96b532`.

Both on-demand playback and Tune in/Rejoin use the same reviewed content and
source attribution. Viewer controls never change the shared schedule. Original
dates remain visible and archived programming is labeled as replay.

The design uses the supplied Democracy Now! vector logo and Amy Goodman photograph, with a dated news archive, readable reporting, and red/black/white styling. Video streams directly from Internet Archive. The app never acquires, proxies, persistently caches, or transcodes Democracy Now! video. Complete source metadata and history stay in its independent engine database.

## Verify and build

Run `make verify` for adapter/tool/asset hashes, frozen dependencies,
typecheck, lint, model tests, and production frontend build. Browser playback,
audible fidelity, shared-channel drift, restore, and deployment remain distinct
checks. Read `AGENTS.md` before changing generated code.

Build the pinned engine image from its source first, or load its verified image
archive. Then build this app:

```sh
docker build --build-arg ENGINE_IMAGE=vhness-engine:9f6ad5b1fa3f20e2c3f063f30ed98d8d4a96b532 \
  -t democracy-now-tv:APP_SOURCE_SHA .
python3 scripts/deploy.py prepare \
  --root ~/.local/state/video-archive/democracy-now-tv --project democracy-now-tv \
  --image democracy-now-tv:APP_SOURCE_SHA --collection democracy_now_vid --port 48072
python3 scripts/deploy.py start \
  --root ~/.local/state/video-archive/democracy-now-tv --project democracy-now-tv \
  --snapshot /absolute/reviewed/democracy-now-tv.dump
```

The helper creates separate private credentials and database state, binds to loopback, and restores snapshots only into an empty owned database. Public ingress remains a separate owner decision. Never reuse another product's secrets or reset an existing database.

See [engine deployment operations](docs/engine-deployment.md) for source refresh, explicit private-library review, seven-day replay planning/renewal, preservation, and rollback. No host timers are installed automatically.

## Assets and software license

This is an independent archive viewer, not an assertion of official affiliation. [Asset provenance](docs/asset-provenance.json) records supplied filenames and hashes. Software follows the engine's GPL-3.0 license; third-party logos, photography, and inspiration retain their separate provenance and are not assigned that software license. Public-release clearance remains separate. Runtime media, metadata snapshots, secrets, and generated evidence stay outside Git.
