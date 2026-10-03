ARG ENGINE_IMAGE=vhness-engine:1980c704e7495557c06fb9e6ac63e47ecc244dab
FROM node:24-bookworm-slim AS frontend
RUN npm install --global pnpm@10.33.0 --force
WORKDIR /src/web
COPY web/package.json web/pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile
COPY web/ ./
RUN pnpm build
FROM ${ENGINE_IMAGE}
COPY --from=frontend /src/web/dist /app/web
