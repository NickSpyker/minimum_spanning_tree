#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <stdbool.h>

/* --- Data Structures --- */

// Adjacency-list edge
typedef struct Edge {
    int v;             // neighbor vertex
    int weight;        // edge weight
    struct Edge *next; // next edge in list
} Edge;

// Heap node storing (vertex, key)
typedef struct {
    int vertex;
    int key;
} HeapNode;

// Min-heap supporting decreaseKey & extractMin
typedef struct {
    int size;        // current heap size
    int capacity;    // total capacity (== number of graph vertices)
    HeapNode *nodes; // 1-based array of heap nodes
    int *pos;        // position map: pos[v] = index of v in nodes[], or 0 if removed
} MinHeap;

/* --- Heap Helper Functions --- */

/**
 * createMinHeap(capacity):
 *   Allocate & return an empty min-heap for 'capacity' vertices.
 */
MinHeap* createMinHeap(int capacity) {
    MinHeap *h = malloc(sizeof(*h));

    h->size     = 0;
    h->capacity = capacity;
    h->nodes    = malloc((capacity + 1) * sizeof(HeapNode)); // 1-based
    h->pos      = calloc(capacity, sizeof(int));             // init to 0

    return h;
}

/**
 * swapHeapNodes(h, i, j):
 *   Exchange nodes[i] <-> nodes[j], updating their pos[] entries.
 */
void swapHeapNodes(MinHeap *h, int i, int j) {
    HeapNode tmp = h->nodes[i];

    h->nodes[i] = h->nodes[j];
    h->nodes[j] = tmp;

    h->pos[h->nodes[i].vertex] = i;
    h->pos[h->nodes[j].vertex] = j;
}

/** 
 * lessThan(a, b):
 *   True if node a has strictly lower key than b,
 *   or equal keys but smaller vertex id (for tie-breaking).
 */
static inline bool lessThan(HeapNode a, HeapNode b) {
    return (a.key != b.key) ? (a.key < b.key) : (a.vertex < b.vertex);
}

/**
 * minHeapify(h, i):
 *   Restore heap property at index i by sifting down.
 */
void minHeapify(MinHeap *h, int i) {
    int smallest = i;
    int left     = 2 * i;
    int right    = 2 * i + 1;

    if (left <= h->size && lessThan(h->nodes[left],  h->nodes[smallest])) {
        smallest = left;
    }

    if (right <= h->size && lessThan(h->nodes[right], h->nodes[smallest])) {
        smallest = right;
    }

    if (smallest != i) {
        swapHeapNodes(h, i, smallest);
        minHeapify(h, smallest);
    }
}

/**
 * buildMinHeap(h):
 *   Turn an arbitrary array of h->nodes[1..size] into a valid heap in O(n).
 */
void buildMinHeap(MinHeap *h) {
    for (int i = h->size / 2; i >= 1; --i) {
        minHeapify(h, i);
    }
}

/** isEmpty(h): return true if no more nodes to extract. */
static inline bool isEmpty(MinHeap *h) {
    return h->size == 0;
}

/**
 * extractMin(h):
 *   Remove & return the root (smallest) node.
 *   Marks its pos[] = 0 so it's no longer "in the heap."
 */
HeapNode extractMin(MinHeap *h) {
    if (isEmpty(h)) {
        fprintf(stderr, "Heap underflow\n");
        exit(EXIT_FAILURE);
    }

    HeapNode root = h->nodes[1];
    int v_root    = root.vertex;

    // Move last node to root, shrink, then heapify
    h->nodes[1] = h->nodes[h->size];
    h->pos[h->nodes[1].vertex] = 1;
    h->pos[v_root] = 0; // mark extracted
    h->size--;

    minHeapify(h, 1);
    return root;
}

/**
 * decreaseKey(h, v, newKey):
 *   Lower the key of vertex v and bubble it up.
 */
void decreaseKey(MinHeap *h, int v, int newKey) {
    int i = h->pos[v];
    if (i == 0 || h->nodes[i].key <= newKey) {
        return;
    }

    h->nodes[i].key = newKey;

    // Bubble up while smaller than parent
    while (i > 1 && lessThan(h->nodes[i], h->nodes[i / 2])) {
        swapHeapNodes(h, i, i / 2);
        i = i / 2;
    }
}

/** inHeap(h, v): true if v not yet extracted (pos[v] != 0). */
static inline bool inHeap(MinHeap *h, int v) {
    return h->pos[v] != 0;
}

/* --- Graph Input & Output --- */

/**
 * addEdge(adj, u, v, w):
 *   Prepend an edge (u->v, weight w) to adjacency list.
 */
void addEdge(Edge **adj, int u, int v, int w) {
    Edge *e = malloc(sizeof(*e));

    e->v      = v;
    e->weight = w;
    e->next   = adj[u];
    adj[u]    = e;
}

/**
 * readGraph(fname, &n, &src):
 *   Reads first line: n m src,
 *   then m lines of "u v w". Builds an undirected graph.
 */
Edge** readGraph(const char *fname, int *n, int *src) {
    FILE *f = fopen(fname, "r");
    if (!f) {
        perror("fopen");
        exit(EXIT_FAILURE);
    }

    int m;
    if (fscanf(f, "%d%d%d", n, &m, src) != 3) {
        fprintf(stderr, "Invalid header in %s\n", fname);
        exit(EXIT_FAILURE);
    }

    Edge **adj = calloc(*n, sizeof(Edge*));
    for (int i = 0, u, v, w; i < m; i++) {
        if (fscanf(f, "%d%d%d", &u, &v, &w) != 3) {
            fprintf(stderr, "Invalid edge at line %d\n", i+2);
            exit(EXIT_FAILURE);
        }
        addEdge(adj, u, v, w);
        addEdge(adj, v, u, w);
    }
    fclose(f);
    return adj;
}

/**
 * writeResult(fname, n, parent[], src):
 *   Outputs each v: "v<TAB>parent[v]\n" or "v<TAB>NIL\n" for the source.
 */
void writeResult(const char *fname, int n, int *parent, int src) {
    FILE *f = fopen(fname, "w");
    if (!f) {
        perror("fopen");
        exit(EXIT_FAILURE);
    }

    for (int v = 0; v < n; v++) {
        if (v == src) {
            fprintf(f, "%d\tNIL\n", v);
        } else {
            fprintf(f, "%d\t%d\n", v, parent[v]);
        }
    }
    fclose(f);
}

/* --- Prim's Algorithm --- */

/**
 * primMST(adj, n, src, parent):
 *   Runs Prim's algorithm with a min-heap in O(m log n).
 *   Fills parent[v] = predecessor of v in the MST.
 */
void primMST(Edge **adj, int n, int src, int *parent) {
    int *key    = malloc(n * sizeof(int));
    MinHeap *h  = createMinHeap(n);

    // 1. Initialize keys & heap array
    for (int v = 0; v < n; v++) {
        key[v] = (v == src ? 0 : INT_MAX);
        parent[v] = -1;
        h->nodes[v+1].vertex = v;
        h->nodes[v+1].key = key[v];
        h->pos[v] = v + 1;
    }
    h->size = n;

    // 2. Build the heap in O(n)
    buildMinHeap(h);

    // 3. Extract-min & relax
    while (!isEmpty(h)) {
        HeapNode mn = extractMin(h);
        int u = mn.vertex;
        for (Edge *e = adj[u]; e; e = e->next) {
            int v = e->v;
            if (inHeap(h, v) && e->weight < key[v]) {
                key[v] = e->weight;
                parent[v] = u;
                decreaseKey(h, v, key[v]);
            }
        }
    }

    free(key);
    free(h->nodes);
    free(h->pos);
    free(h);
}

/* --- Main --- */

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <input_file> <output_file>\n", argv[0]);
        return EXIT_FAILURE;
    }

    int n       = 0;
    int src     = 0;
    Edge **adj  = readGraph(argv[1], &n, &src);
    int *parent = malloc(n * sizeof(int));

    primMST(adj, n, src, parent);
    writeResult(argv[2], n, parent, src);

    // Free adjacency lists
    for (int u = 0; u < n; u++) {
        Edge *e = adj[u];
        while (e) {
            Edge *tmp = e;
            e = e->next;
            free(tmp);
        }
    }
    free(adj);
    free(parent);
    return EXIT_SUCCESS;
}
