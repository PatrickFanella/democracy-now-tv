# Standalone video app

This repository owns its frontend, design system and deployment configuration.
The shared engine source is VHNESS. web/src/engine is a generated adapter pinned
by manifest.json; never edit it here. Export a reviewed engine revision, verify
the manifest and qualify playback before upgrading.

Run make verify. Browser rendering, decoding, audiovisual review, shared-channel
timing, independent restore and deployment are separate checks. Runtime data,
media and secrets stay outside Git. Public deployment requires its separate
owner decision. Preserve original dates, source credit and replay labels.
