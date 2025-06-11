# Minimum Spanning Tree

## Structurs

```c
typedef struct {
    int v;
    int weight;
} Edge;

typedef struct {
    int vertex;
    int key;
    int parent;
} HeapNode;
```

## Functions Comments

```c
// Swaps two HeapNode elements in the heap.
// Parameters:
//   a - pointer to the first HeapNode
//   b - pointer to the second HeapNode
void swap(HeapNode* a, HeapNode* b);

// Ensures the min-heap property for the subtree rooted at index i.
// Parameters:
//   i - index of the subtree root in the heap array
void minHeapify(int i);

// Removes and returns the vertex with the minimum key value from the heap.
// Returns:
//   The vertex ID with the minimum key value.
int extractMin();

// Decreases the key value of a given vertex in the heap and restores heap property.
// Parameters:
//   v      - vertex ID whose key is to be decreased
//   newKey - new key value to assign
void decreaseKey(int v, int newKey);

// Inserts a new vertex with a given key value into the heap.
// Parameters:
//   v - vertex ID to insert
//   k - key value for the vertex
void insertHeap(int v, int k);

// Executes Prim's algorithm using a min-heap to find the Minimum Spanning Tree.
// Parameters:
//   start - starting vertex for Prim's algorithm
void prim(int start);

// Main function: reads input, builds the adjacency matrix, runs Prim's algorithm, and writes output.
// Parameters:
//   argc - argument count
//   argv - argument vector (expects input and output file names)
// Returns:
//   0 on success, 1 on error
int main(int argc, char* argv[]);
```
