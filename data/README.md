# Minimum Spanning Tree Test Cases

This directory contains test cases for the minimum spanning tree implementation using Prim's algorithm.

## Input Format

Each input file follows this format:

```
[num_vertices]<tab>[num_edges]<tab>[start vertex ID]
[vertex ID]<tab>[vertex ID]<tab>[weight]
[vertex ID]<tab>[vertex ID]<tab>[weight]
...
```

## Output Format

Each output file follows this format:

```
[vertex ID]<tab>[predecessor]
[vertex ID]<tab>[predecessor]
...
```

Where `NIL` indicates the root vertex of the MST.

## Test Cases

1. **input_mst_0.txt / output_mst_0.txt**:
   - Standard example from the specifications
   - 9 vertices, 14 edges
2. **input_mst_1.txt / output_mst_1.txt**:
   - Small graph with 5 vertices and 7 edges
   - Simple connected graph
3. **input_mst_2.txt / output_mst_2.txt**:
   - Complete graph with 6 vertices (all vertices connected to each other)
   - 15 edges with various weights
4. **input_mst_3.txt / output_mst_3.txt**:
   - Disconnected graph with 8 vertices forming two separate components
   - Tests minimum spanning forest scenario
5. **input_mst_4.txt / output_mst_4.txt**:
   - Larger graph with 10 vertices and 20 edges
   - More complex connectivity
6. **input_mst_5.txt / output_mst_5.txt**:
   - Graph with 7 vertices where multiple edges have the same weight
   - Tests tie-breaking in the algorithm
