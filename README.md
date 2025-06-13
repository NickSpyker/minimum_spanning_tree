# Minimum Spanning Tree

Implementation of Prim's algorithm for finding the minimum spanning tree of an undirected graph.

## Overview

This project implements Prim's algorithm using a binary heap-based priority queue to find the minimum spanning tree of an undirected graph.
The implementation includes the following operations:

- Extract-Min
- Decrease-Key
- Min-Heapify
- Insertion

## Building and Running

### Prerequisites

- C compiler with GCC
- Python 3 (for running tests)

### Building

To build the project, run:

```bash
make
```

This will compile the source code and generate the executable `mst`.

### Running

To run the program with the default input and output files:

```bash
make run
```

Or to run with custom input and output files:

```bash
./mst <input_file> <output_file>
```

## Input and Output Format

### Input File Format

```
[num_vertices]<tab>[num_edges]<tab>[start vertex ID]
[vertex ID]<tab>[vertex ID]<tab>[weight]
[vertex ID]<tab>[vertex ID]<tab>[weight]
...
```

Example:

```
9	14	0
0	1	4
0	7	8
1	2	8
...
```

### Output File Format

```
[vertex ID]<tab>[predecessor]
[vertex ID]<tab>[predecessor]
...
```

Example:

```
0	NIL
1	0
2	1
...
```

## Testing

The project includes a comprehensive test suite to verify the correctness and performance of the implementation.

### Running Tests

To run all tests:

```bash
make test
```

To run only performance tests:

```bash
make test-performance
```

See the [test directory README](./test/README.md) for more details on the test suite.

## Documentation

For more detailed information about the algorithm and implementation, see the [specifications document](./docs/specifications.md).

## Cleaning Up

To clean up the build artifacts:

```bash
make clean
```

This will remove the executable and any object files.
