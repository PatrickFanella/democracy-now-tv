# Viewer audit, October 6, 2026

This product pins published viewer 0.4.0, core 0.3.0 and engine 0.4.0,
with registry integrity and immutable receipts from Arkhiv source
39a49fb45005b001e14218823c22ed19c3de1177. Complete make verify passed in
an isolated snapshot using this consumer's frozen registry lock, outside
the engine workspace. Hosted CI is waived while Kvant is down.

Grid/table preference previously reset on reload. The consumer now stores
the preference by collection and retains the current view in memory when
storage writes fail. Browser checks used consumer-owned markup against the
separate vhness-local-fixture collection, generated video and private account
services. Production collection constants were untouched. These checks do
not establish real source audiovisual fidelity or physical device behavior.

Bill Nye table selection survived reload. Democracy Now! rendered the semantic
table and retained a selected local favorite after reload. The template switched
grid/table using Enter with visible focus. A missing search returned an explicit
empty state; an injected catalog-only 503 rendered an alert, and restoring the
route recovered results. Storage write denial retained current view and favorite
changes in memory, but the favorite UI did not disclose that those changes were
temporary. That shared follow-up remains necessary before browsing issue closure.

Accounts/chat stay optional. iOS verification is unavailable without macOS/Xcode;
Android verification is unavailable without the SDK. Real source playback,
remaining boundary/suspension checks, cross-device sync and provider activation
retain their separate evidence requirements.

## Shared storage patch

Viewer 0.4.1 was independently published from Arkhiv source
14dd96bb216bb6e3a1331e65dbb3f6ebadbd4dff. The registry receipt is in
deploy/viewer-release.json. Core 0.3.0 and engine 0.4.0 receipts remain intact.
Browser checks on the packed SDK showed the temporary-favorites warning after
a rejected write and warning removal after a successful write. The shared hook
also retains newer pending edits across remounts. This adoption requires the
updated consumer frozen-lock gate; it changes no live deployment.

The complete consumer make verify passed with SDK 0.4.1 and this frozen registry lock. Native print integrations used disposable PostgreSQL 15 matching the dump client. Frontend receipt verification is independent of the retained core and reference-engine image receipts.

## Volume preference browser qualification

The October 6 independently built bundle restored origin-wide volume 0.30 and mute=true in the actual T3 browser against generated fixture playback. Bill Nye additionally retained those values across channel boundaries, channel/on-demand switches, two episodes, reload and keyboard slider changes. Template qualified invalid-value fallback, denied storage remount and controlled autoplay denial/manual retry. See Arkhiv `docs/reports/volume-qualification-2026-10-06.md`; #108 still owns suspension/drift qualification. Production collection constants and deployment remain unchanged.

## Artwork component adoption

The independently built bundle decoded the retained Bill Nye shared source thumbnail to 192 × 141 pixels in both library cards, showing `Series artwork` and preserving accessible episode action names. This used an explicitly identified browser-only image projection onto generated fixture records; no backend artwork decision, media acquisition or live product deployment occurred. The reference viewer additionally qualified actual source-image failure with text/date fallback. See Arkhiv `docs/reports/artwork-qualification-2026-10-06.md`.
