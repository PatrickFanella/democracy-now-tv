.PHONY: verify
verify: verify-core-pin
	python3 scripts/check_engine.py
	pnpm --dir web install --frozen-lockfile
	pnpm --dir web typecheck
	pnpm --dir web lint
	pnpm --dir web test
	pnpm --dir web build

.PHONY: verify-core-pin
verify-core-pin:
	python3 scripts/check_core_pin.py
