# Minimum Spanning Tree Test Cases

This directory contains test cases for the Minimum Spanning Tree (MST) implementation using Prim's algorithm.

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

### Test Case 0: Standard Example

- **Source**: Example from the assignment specification
- **Description**: A 9-vertex graph with 14 edges
- **Files**: `input_mst_0.txt` / `output_mst_0.txt`

#### Input

```mermaid
graph LR
  0 -- "4" --- 1
  0 -- "8" --- 7
  1 -- "8" --- 2
  1 -- "11" --- 7
  2 -- "7" --- 3
  2 -- "4" --- 5
  2 -- "2" --- 8
  3 -- "9" --- 4
  3 -- "14" --- 5
  4 -- "10" --- 5
  5 -- "2" --- 6
  6 -- "1" --- 7
  6 -- "6" --- 8
  7 -- "7" --- 8
```

#### Output

```mermaid
graph LR
  0 -- "4" --- 1
  1 -- "8" --- 2
  2 -- "7" --- 3
  3 -- "9" --- 4
  2 -- "4" --- 5
  5 -- "2" --- 6
  6 -- "1" --- 7
  2 -- "2" --- 8
```

### Test Case 1: Small Graph

- **Source**: Custom example
- **Description**: A small 4-vertex graph with 5 edges
- **Files**: `input_mst_1.txt` / `output_mst_1.txt`

#### Input

```mermaid
graph LR
  0 -- "10" --- 1
  0 -- "6" --- 2
  0 -- "5" --- 3
  1 -- "15" --- 3
  2 -- "4" --- 3
```

#### Output

```mermaid
graph LR
  0 -- "10" --- 1
  3 -- "4" --- 2
  0 -- "5" --- 3
```

### Test Case 2: Medium Graph

- **Source**: Custom example
- **Description**: A 7-vertex graph with 12 edges
- **Files**: `input_mst_2.txt` / `output_mst_2.txt`

#### Input

```mermaid
graph LR
  0 -- "2" --- 1
  0 -- "1" --- 3
  1 -- "3" --- 2
  1 -- "2" --- 3
  1 -- "10" --- 4
  2 -- "7" --- 4
  2 -- "5" --- 5
  3 -- "9" --- 4
  3 -- "4" --- 6
  4 -- "1" --- 5
  4 -- "8" --- 6
  5 -- "6" --- 6
```

#### Output

```mermaid
graph LR
  0 -- "2" --- 1
  1 -- "3" --- 2
  0 -- "1" --- 3
  5 -- "1" --- 4
  2 -- "5" --- 5
  3 -- "4" --- 6
```

### Test Case 3: Medium-Large Graph

- **Source**: Custom example
- **Description**: A 10-vertex graph with 15 edges
- **Files**: `input_mst_3.txt` / `output_mst_3.txt`

#### Input

```mermaid
graph LR
  0 -- "10" --- 1
  0 -- "12" --- 2
  1 -- "9" --- 2
  1 -- "8" --- 3
  2 -- "3" --- 3
  2 -- "1" --- 5
  3 -- "7" --- 4
  3 -- "10" --- 5
  4 -- "5" --- 5
  4 -- "6" --- 6
  5 -- "2" --- 6
  5 -- "4" --- 7
  6 -- "8" --- 7
  7 -- "14" --- 8
  7 -- "9" --- 9
```

#### Output

```mermaid
graph LR
  0 -- "10" --- 1
  3 -- "3" --- 2
  1 -- "8" --- 3
  5 -- "5" --- 4
  2 -- "1" --- 5
  5 -- "2" --- 6
  5 -- "4" --- 7
  7 -- "14" --- 8
  7 -- "9" --- 9
```

### Test Case 4: Large Graph

- **Source**: Custom example
- **Description**: A 15-vertex graph with 21 edges
- **Files**: `input_mst_4.txt` / `output_mst_4.txt`

#### Input

```mermaid
graph LR
  0 -- "4" --- 1
  0 -- "3" --- 2
  1 -- "5" --- 2
  1 -- "2" --- 3
  2 -- "6" --- 3
  2 -- "8" --- 4
  3 -- "7" --- 4
  3 -- "1" --- 5
  4 -- "9" --- 5
  4 -- "4" --- 6
  5 -- "5" --- 6
  6 -- "3" --- 7
  6 -- "2" --- 8
  7 -- "6" --- 8
  8 -- "7" --- 9
  9 -- "5" --- 10
  10 -- "4" --- 11
  11 -- "3" --- 12
  12 -- "8" --- 13
  12 -- "9" --- 14
  13 -- "2" --- 14
```

#### Output

```mermaid
graph LR
  0 -- "4" --- 1
  0 -- "3" --- 2
  1 -- "2" --- 3
  6 -- "4" --- 4
  3 -- "1" --- 5
  5 -- "5" --- 6
  6 -- "3" --- 7
  6 -- "2" --- 8
  8 -- "7" --- 9
  9 -- "5" --- 10
  10 -- "4" --- 11
  11 -- "3" --- 12
  12 -- "8" --- 13
  13 -- "2" --- 14
```
