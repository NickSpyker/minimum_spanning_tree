# Minimum Spanning Tree Implementation

This project implements Prim's algorithm for finding the Minimum Spanning Tree (MST) of a graph.

## Algorithm

The implementation uses Prim's algorithm with a binary heap-based priority queue to efficiently find the MST of an undirected graph. The time complexity is O(E log V), where E is the number of edges and V is the number of vertices.

## Features

- Binary heap-based priority queue with Extract-Min, Decrease-Key, and Insert operations
- Efficient implementation of Prim's algorithm
- Support for reading graph input files and writing MST output files
- Comprehensive test suite with various graph examples

## Usage

```bash
# Compile the program
make

# Run the program with input and output files
./mst input_mst.txt output_mst.txt

# Run the test suite
make test

# Clean up generated files
make clean
```

## Input Format

The input files follow this format:

```
[num_vertices]<tab>[num_edges]<tab>[start vertex ID]
[vertex ID]<tab>[vertex ID]<tab>[weight]
[vertex ID]<tab>[vertex ID]<tab>[weight]
...
```

## Output Format

The output files follow this format:

```
[vertex ID]<tab>[predecessor]
[vertex ID]<tab>[predecessor]
...
```

Where `NIL` is used to indicate the root vertex (no predecessor).

## Test Cases

The project includes several test cases:

1. Standard example from the assignment specification
2. Small graph with 4 vertices and 5 edges
3. Medium graph with 7 vertices and 12 edges
4. Medium-large graph with 10 vertices and 15 edges
5. Large graph with 15 vertices and 21 edges
6. GeeksForGeeks MST example

For more details on the test cases, see `data/README.md`.

## Implementation Details

The implementation includes:

- An adjacency list representation of the graph
- A binary min-heap for the priority queue
- Efficient heap operations (extract-min, decrease-key)
- Prim's algorithm for MST computation

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
