ARG ENGINE_IMAGE=vhness-engine:9f6ad5b1fa3f20e2c3f063f30ed98d8d4a96b532
FROM node:24-bookworm-slim AS frontend
RUN npm install --global pnpm@10.33.0 --force
WORKDIR /src/web
COPY web/package.json web/pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile
COPY web/ ./
RUN pnpm build
FROM ${ENGINE_IMAGE}
COPY --from=frontend /src/web/dist /app/web
