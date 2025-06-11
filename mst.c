#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAXV (int) 1000

typedef struct {
    int v;
    int weight;
} Edge;

typedef struct {
    int vertex;
    int key;
    int parent;
} HeapNode;

Edge* graph[MAXV][MAXV];
int num_vertices;
int num_edges;
int start;
int adj[MAXV][MAXV];
int key[MAXV];
int parent[MAXV];
int inMST[MAXV];

int heapSize = 0;
HeapNode heap[MAXV];

// Swaps two HeapNode elements in the heap.
// Parameters:
//   a - pointer to the first HeapNode
//   b - pointer to the second HeapNode
void swap(HeapNode* a, HeapNode* b) {
    HeapNode tmp = *a;
    *a = *b;
    *b = tmp;
}

// Ensures the min-heap property for the subtree rooted at index i.
// Parameters:
//   i - index of the subtree root in the heap array
void minHeapify(int i) {
    int l = 2 * i + 1;
    int r = 2 * i + 2;
    int smallest = i;

    if (l < heapSize && heap[l].key < heap[smallest].key) {
        smallest = l;
    }
    if (r < heapSize && heap[r].key < heap[smallest].key) {
        smallest = r;
    }
    if (smallest != i) {
        swap(&heap[i], &heap[smallest]);
        minHeapify(smallest);
    }
}

// Removes and returns the vertex with the minimum key value from the heap.
// Returns:
//   The vertex ID with the minimum key value.
int extractMin() {
    int minV = heap[0].vertex;
    heap[0] = heap[--heapSize];
    minHeapify(0);
    return minV;
}

// Decreases the key value of a given vertex in the heap and restores heap property.
// Parameters:
//   v      - vertex ID whose key is to be decreased
//   newKey - new key value to assign
void decreaseKey(int v, int newKey) {
    for (int i = 0; i < heapSize; i++) {
        if (heap[i].vertex != v) {
            continue;
        }
        heap[i].key = newKey;
        while (i > 0 && heap[(i - 1) / 2].key > heap[i].key) {
            swap(&heap[i], &heap[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
        break;
    }
}

// Inserts a new vertex with a given key value into the heap.
// Parameters:
//   v - vertex ID to insert
//   k - key value for the vertex
void insertHeap(int v, int k) {
    int i = heapSize++;

    heap[i].vertex = v;
    heap[i].key = k;
    while (i > 0 && heap[(i - 1) / 2].key > heap[i].key) {
        swap(&heap[i], &heap[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

// Executes Prim's algorithm using a min-heap to find the Minimum Spanning Tree.
// Parameters:
//   start - starting vertex for Prim's algorithm
void prim(int start) {
    for (int i = 0; i < num_vertices; i++) {
        key[i] = INT_MAX;
        parent[i] = -1;
        inMST[i] = 0;
    }

    key[start] = 0;

    for (int v = 0; v < num_vertices; v++) {
        insertHeap(v, key[v]);
    }

    while (heapSize > 0) {
        int u = extractMin();
        inMST[u] = 1;
        for (int v = 0; v < num_vertices; v++) {
            if (adj[u][v] && !inMST[v] && adj[u][v] < key[v]) {
                key[v] = adj[u][v];
                parent[v] = u;
                decreaseKey(v, key[v]);
            }
        }
    }
}

// Main function: reads input, builds the adjacency matrix, runs Prim's algorithm, and writes output.
// Parameters:
//   argc - argument count
//   argv - argument vector (expects input and output file names)
// Returns:
//   0 on success, 1 on error
int main(int argc, char* argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s input.txt output.txt\n", argv[0]);
        return 1;
    }

    FILE* fin = fopen(argv[1], "r");
    FILE* fout = fopen(argv[2], "w");

    if (fscanf(fin, "%d %d %d", &num_vertices, &num_edges, &start) != 3) {
        fprintf(stderr, "Error: Failed to read num_vertices, num_edges, or start from input file.\n");
        fclose(fin);
        fclose(fout);
        return 1;
    }

    for (int i = 0; i < num_edges; i++) {
        int u;
        int v;
        int w;

        if (fscanf(fin, "%d %d %d", &u, &v, &w) != 3) {
            fprintf(stderr, "Error: Failed to read edge %d from input file.\n", i);
            fclose(fin);
            fclose(fout);
            return 1;
        }

        adj[u][v] = w;
        adj[v][u] = w;
    }

    prim(start);

    for (int i = 0; i < num_vertices; i++) {
        if (parent[i] == -1) {
            fprintf(fout, "%d\tNIL\n", i);
        } else {
            fprintf(fout, "%d\t%d\n", i, parent[i]);
        }
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
