ARG := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARG):;@:)

check:
	@uv run ruff check

# example: make test 01
test:
	@uv run pytest -q ./src/day$(ARG)/main.py

# example: make run 01
run:
	@uv run ./src/day$(ARG)/main.py

# example: make watch 01
watch:
	@uv run pymon -c -p "*.py;*.txt" ./src/day$(ARG)/main.py
