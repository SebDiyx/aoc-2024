# Set up

Install `uv`

```bash
curl -LsSf <https://astral.sh/uv/install.sh> | sh
```

install `make`

```bash
sudo apt-get update
sudo apt-get install make
```

# Make commands

Run tests for a given day

```bash
make test <day number>
```

Run answer file for a given day

```bash
make run <day number>
```

Run answer file in watch mode for a given day

```bash
make watch <day number>
```
