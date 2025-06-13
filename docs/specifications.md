# Algorithm

## Assignment 2: Minimum Spanning Tree

> Chung-Ang University
> School of Computer Science and Engineering
> 2025 Spring
> Yunyong Ko

### **Goal**: To Implement Prim’s Algorithm

- Binary heap-based priority queue
  - Extract-Min
  - Decrease-Key
  - Insert, Min-Heapify

```
MST-PRIM(G, w, r)
    for each u ∈ G.V
        u.key = ∞
        u.π = NIL
    r.key = 0
    Q = G.V (Insert)
    while Q ≠ ∅
        u = EXTRACT-MIN(Q) (Extract-Min)
        for each v ∈ G.Adj[u]
            if v ∈ Q and w(u, v) < v.key
                v.π = u
                v.key = w(u, v) (Decrease-Key)
```

### Functions to implement

- **`Extract-Min` (deletion):** O(log n)
  - (1) Extract the element with the highest priority (minimum)
  - (2) Reorganize the priority queue using `Min-Heapify()`
- **`Min-Heapify`:** O(log n)
  - Revise the `Max-Heapify` function

> All elements in `{...}` should be revised

```
HEAP-EXTRACT-{MAX}(A)
    if A.heap-size < 1
        error "heap underflow"
    {max} = A[1]
    A[1] = A[A.heap-size]
    A.heap-size = A.heap-size - 1
    {MAX-HEAPIFY(A, 1)}
    return {max}
```

> All elements in `{...}` should be revised

```
MAX-HEAPIFY(A, i)
    l = LEFT(i)
    r = RIGHT(i)
    if l ≤ A.heap-size and {A[l] > A[i]}
        largest = l
    else largest = i
    if r ≤ A.heap-size and {A[r] > A[largest]}
        largest = r
    if largest ≠ i
        exchange A[i] with A[largest]
    MAX-HEAPIFY(A, largest)
```

- **`Decrease-Key`:** O(log n)
  - Decrease the value of `x`'s key to the new value `k`
  - Traverse a path from x to the root to find a proper place for the newly decreased key
    - (1) Compare its key with its parent’s key
    - (2) Decide whether exchanging their keys
- **`Insertion`:** O(log n)
  - (1) Expand the min-heap by adding a new leaf node
  - (2) Call `Decrease_Key(A, A.size, key)`
    - To set the value of the new leaf node's key
    - To maintain the min-heap property

> All elements in `{...}` should be revised
> Revise the Increase-Key function

```
HEAP-INCREASE-KEY(A, i, key)
    if key < A[i]
        error "new key is smaller than current key"
    A[i] = key
    while i > 1 and {A[PARENT(i)] < A[i]}
        exchange A[i] with A[PARENT(i)]
        i = PARENT(i)
```

> All elements in `{...}` should be revised

```
MAX-HEAP-INSERT(A, key)
    A.heap-size = A.heap-size + 1
    A[A.heap-size] = -∞
    {HEAP-INCREASE-KEY(A, A.heap-size, key)}
```

### Description: Input and Output Files

#### Input file (Undirected Graph)

> Make your own input files by yourself

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
1	7	11
2	3	7
2	5	4
2	8	2
3	4	9
3	5	14
4	5	10
5	6	2
6	7	1
6	8	6
7	8	7
```

#### Output file (Prim's algorithm)

```
[vertex ID]<tab>[predecessor]
[vertex ID]<tab>[predecessor]
...
```

Exemple:

```
0	NIL
1	0
2	1
3	2
4	3
5	2
6	5
7	6
8	2
```

### Makefile

> Please make sure that your code is compiled and run successfully, and the results in the output file are correct

- `make` will compile your code and generate the executable file (e.g., gcc mst.c –o mst)
- `make run` will run your program (./mst input_mst.txt output_mst.txt)
  - 2 filenames: 1 input files and 1 output files
- `make clean` will delete the executable file and output file (e.g., rm mst output_mst.txt)

### Evaluation Aspects

- **Makefile**
  - Carefully check whether your code run without error
- **Results on Test Input Files**
  - Your code should generate a correct output
  - Make various test input files by yourself and test your code a lot
- **Documentation**
  - Comments for All Functions that You Implemented
    - Writing comments in Korean is allowed (문서로는한글로작성가능)
  - Attach screenshots to show that your program runs well
  - .pdf format is only allowed

### Submission Guideline

- **Submission**
  - What: Compressed file (Source code, Your input file, makefile, document (.pdf))
  - Filename: Assignment2_StudentID
  - Compress the four files together, NOT your workspace directory
    - Or name your workspace directory as Assignment4_studentID
  - Where: Assignment board on e-class
  - Deadline: 11:59 PM, June 15th (Sunday), 2025
- **Late submission:** ~ June 17th (Sunday), 2024 (+1 day: -25%, +2 day: -50%, +3 day: no score)
- **Q&A**
  - Office hour: 2:00 PM, Friday
  - Contact Information
    - Email: yyko@cau.ac.kr
    - Tel: 02-820-5507
