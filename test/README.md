# MST Tests

This directory contains functional tests for the Minimum Spanning Tree (MST) implementation.

## Running Tests

You can run the tests using the following methods:

### Using Make

```bash
make test              # Run all tests
make test-performance  # Run only performance tests
```

This will compile the MST program if needed and run the tests.

### Running Tests Directly

```bash
python3 ./test/run_tests.py
```

Or run individual test files:

```bash
python3 ./test/test_mst.py
python3 ./test/test_complex_graphs.py
python3 ./test/test_performance.py
```

## Test Description

The test suite includes:

1. **Basic Tests** (`test_mst.py`):
   - Tests against all provided input/output pairs in the data directory
   - Tests for edge cases like empty graphs and single-edge graphs
2. **Complex Graph Tests** (`test_complex_graphs.py`):
   - Tests for disconnected graphs
   - Tests for complete graphs
3. **Performance Tests** (`test_performance.py`):
   - Tests with increasing graph sizes to verify time complexity
   - Tests with varying edge densities (sparse vs. dense graphs)
   - Validates that the implementation maintains the expected O(E log V) time complexity

## Adding New Tests

To add new tests:

1. Create a new Python file in the test directory with a name starting with `test_`
2. Extend the `unittest.TestCase` class
3. Add test methods that start with `test_`

The test runner will automatically discover and run these tests.
