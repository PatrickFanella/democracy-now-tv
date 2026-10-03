.PHONY: verify
verify:
	python3 scripts/check_engine.py
	pnpm --dir web install --frozen-lockfile
	pnpm --dir web typecheck
	pnpm --dir web lint
	pnpm --dir web test
	pnpm --dir web build
