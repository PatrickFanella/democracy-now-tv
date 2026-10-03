# syntax=docker/dockerfile:1
ARG ENGINE_IMAGE
FROM node:24-bookworm-slim AS frontend
RUN npm install --global pnpm@10.33.0 --force
WORKDIR /src/web
COPY web/package.json web/pnpm-lock.yaml ./
RUN --mount=type=secret,id=npmrc,required=true NPM_CONFIG_USERCONFIG=/run/secrets/npmrc pnpm install --frozen-lockfile
COPY web/ ./
RUN pnpm build
FROM ${ENGINE_IMAGE}
COPY --from=frontend /src/web/dist /app/web
