# Optional personal preferences and discussion

This product owns its sign-in prompts, local favorite storage, import review,
chat panel, moderation interface and session-service configuration. Anonymous
viewing works without these services. Configure no live provider or public
posting until the owner selects the provider/client, hosting, recovery target
and moderator coverage.

The frontend imports the released `usePersonal` and `useChannelChat` contracts.
Same-origin `/api/account/v1`, `/api/personal/v1` and `/api/chat/v1` routes go to
the product's session service. Archive routes continue to use the core API.
The optional `deploy/community-compose.yml` overlay and
`deploy/community-nginx.conf` supply that routing for the API-only core lane.
Load the normal core Compose file first, then the optional overlay. The base
deployment keeps accounts and chat disabled.

Provision a separate personal database and restricted runtime role using the
[shared community contract](https://git.subcult.tv/subculture-collective/arkhiv/src/branch/feat/improve-video-viewing/docs/reference/community.md).
Prepare owner-only config, key and connection files outside Git. The configured
paths must match the overlay's secret mounts. Use this product's deployment ID,
origin, collection and independently appointed moderator roster. Set the
recovery directory to `/independent-recovery/personal-events`; retain and
replicate that directory independently of the database and 35-day dump rotation.
The overlay does not provision or migrate an external personal database.

Keep `chat_read` and `chat_post` false during setup. Sign-in is optional. Imports
show the count and destination, preserve the local copy and prepare reviewable
pending changes. Conflicts and offline failures keep pending records for explicit
retry. Signing out preserves browser favorites. Deleting the product account
requires recent sign-in and confirmation; it does not delete the provider
account or archive records.

Messages are plain text and carry their replay program and original date.
On-demand and paused viewers can read discussion but must rejoin the current
channel before posting. Reports stay private. User blocks, own-message deletion
and separately authorized moderator withdrawal/restriction controls are included.
The accepted retention periods are 30 days for discussion, 35 days for personal
backups and 90 days for opaque deletion evidence. Qualify these operations and
restore suppression before any public activation.

Sharing offers the native browser sheet, a copyable link, email and the documented [Bluesky compose intent](https://bsky.network/docs/intent-links/). Opening an intent leaves posting confirmation to the user.

## Release qualification

This branch pins published `@subcult/archive-viewer@0.3.0` and core `0.2.0`
from Arkhiv commit `929401fdd693ece1ae5d38c8c4c035bcb3712dd8`, with registry
integrity and immutable image receipts. The repository's full `make verify`
passed in an isolated T3 snapshot. The optional Compose overlay rendered without
starting services. Hosted CI and remaining browser qualification are outstanding;
these checks do not activate a provider or deploy the product publicly.
