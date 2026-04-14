#!/bin/bash

# Configuration specified by SCORER_GUIDE.md
ROOT="$(pwd)"
TIMEOUT=15

# Compilation is a no-op since Python does not compile
compile() {
  return 0
}

# Run the checker logic and let it produce `PASS` or `FAIL: <reason>`
run() {
  python3 "$ROOT/tests/checker.py"
}
