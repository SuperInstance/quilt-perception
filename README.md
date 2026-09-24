# quilt-perception

> Perception substrate — routes sensor data through 6 perception slots

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)]()
[![Tests](https://img.shields.io/badge/tests-6+-brightgreen.svg)](tests/)
[![Brewed by](https://img.shields.io/badge/brewed_by-quilt--brewer-purple.svg)](https://github.com/SuperInstance/quilt-brewer)

## What is this?

Brewed by `quilt-brewer` from the `quilt-perception` recipe. Implements the
canonical substrate walker pattern (199 LOC wrapper + tests + demo).

## Polarity rules

| Polarity | Status |
|---|---|
| **ACCEPT** | `ok` |
| **DRIFT** | `warn` |
| **REFUSE** | `fail` |

## Operations

- ingest
- classify
- route
- summarize

## Usage

```python
from quilt_perception import SensorStreamSubstrate

substrate = SensorStreamSubstrate()
receipt = substrate.step("cell-id", {"key": "value"}, status="ok")
print(receipt.polarity)  # ACCEPT
```

## Run tests

```bash
python3 -m unittest tests.test_sensor_stream -v
```

## Run demo

```bash
python3 examples/demo.py
```

## License

Apache-2.0
