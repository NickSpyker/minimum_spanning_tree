#!/usr/bin/env python3
import os
import subprocess
import unittest
import tempfile
import time
import random

class TestPerformance(unittest.TestCase):
    """
    Test suite for benchmarking the performance of the MST implementation.
    """

    @classmethod
    def setUpClass(cls):
        # Compile the program if it doesn't exist
        if not os.path.exists("mst"):
            subprocess.run(["make"], check=True)

    def generate_random_graph(self, num_vertices, edge_density=0.3, max_weight=100):
        """Generate a random graph with the given number of vertices and edge density."""
        # Calculate number of edges based on density
        # For a complete graph, max edges = n(n-1)/2
        max_edges = (num_vertices * (num_vertices - 1)) // 2
        num_edges = int(max_edges * edge_density)

        # Ensure the graph is connected by including a spanning tree
        edges = []
        for i in range(1, num_vertices):
            # Connect vertex i to a random vertex from [0, i-1]
            j = random.randint(0, i-1)
            weight = random.randint(1, max_weight)
            edges.append((j, i, weight))

        # Add remaining random edges
        remaining_edges = num_edges - (num_vertices - 1)
        if remaining_edges > 0:
            # Create a list of all possible edges not in the spanning tree
            all_edges = [(u, v) for u in range(num_vertices) for v in range(u+1, num_vertices)]
            # Remove edges already in the spanning tree
            for u, v, _ in edges:
                if u > v:
                    u, v = v, u
                if (u, v) in all_edges:
                    all_edges.remove((u, v))

            # Randomly select remaining edges
            if len(all_edges) > remaining_edges:
                random_edges = random.sample(all_edges, remaining_edges)
                for u, v in random_edges:
                    weight = random.randint(1, max_weight)
                    edges.append((u, v, weight))

        return num_vertices, len(edges), edges

    def test_performance_increasing_vertices(self):
        """Test MST implementation with increasing number of vertices."""
        vertex_counts = [10, 50, 100, 200]
        timings = []

        for num_vertices in vertex_counts:
            # Generate a random graph
            n, m, edges = self.generate_random_graph(num_vertices)

            # Create a temporary input file
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_in:
                tmp_in.write(f"{n}\t{m}\t0\n")  # Start at vertex 0
                for u, v, w in edges:
                    tmp_in.write(f"{u}\t{v}\t{w}\n")
                temp_input = tmp_in.name

            # Create a temporary output file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_out:
                temp_output = tmp_out.name

            try:
                # Measure execution time
                start_time = time.time()
                result = subprocess.run(
                    ["./mst", temp_input, temp_output],
                    capture_output=True,
                    text=True,
                    check=True
                )
                end_time = time.time()

                execution_time = end_time - start_time
                timings.append((num_vertices, execution_time))

                print(f"Vertices: {num_vertices}, Edges: {m}, Time: {execution_time:.6f} seconds")

                # Basic validation - check if output file has correct number of lines
                with open(temp_output, 'r') as f:
                    lines = f.readlines()
                    self.assertEqual(len(lines), num_vertices, 
                                    f"Output should have {num_vertices} lines")
            finally:
                # Clean up the temporary files
                for file in [temp_input, temp_output]:
                    if os.path.exists(file):
                        os.unlink(file)

        # Check that time complexity is roughly O(E log V)
        # This is just a basic check - not a strict mathematical proof
        if len(timings) > 1:
            for i in range(1, len(timings)):
                v1, t1 = timings[i-1]
                v2, t2 = timings[i]

                # Calculate expected ratio based on O(E log V) complexity
                # Assuming E ~ V^2 * edge_density, the ratio should be roughly:
                # (V2^2 * log V2) / (V1^2 * log V1)
                expected_ratio = (v2**2 * (v2).bit_length()) / (v1**2 * (v1).bit_length())
                actual_ratio = t2 / t1 if t1 > 0 else float('inf')

                # Allow for some variance in the timing measurements
                # The actual ratio should be within an order of magnitude of the expected ratio
                self.assertTrue(
                    0.1 * expected_ratio <= actual_ratio <= 10 * expected_ratio,
                    f"Time complexity doesn't match O(E log V): {actual_ratio} vs {expected_ratio}"
                )

    def test_performance_dense_vs_sparse(self):
        """Test MST implementation with dense vs sparse graphs of the same size."""
        num_vertices = 100
        densities = [0.1, 0.5, 0.9]  # Sparse, medium, dense

        for density in densities:
            # Generate a random graph with the given density
            n, m, edges = self.generate_random_graph(num_vertices, edge_density=density)

            # Create a temporary input file
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_in:
                tmp_in.write(f"{n}\t{m}\t0\n")  # Start at vertex 0
                for u, v, w in edges:
                    tmp_in.write(f"{u}\t{v}\t{w}\n")
                temp_input = tmp_in.name

            # Create a temporary output file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_out:
                temp_output = tmp_out.name

            try:
                # Measure execution time
                start_time = time.time()
                result = subprocess.run(
                    ["./mst", temp_input, temp_output],
                    capture_output=True,
                    text=True,
                    check=True
                )
                end_time = time.time()

                execution_time = end_time - start_time
                print(f"Density: {density:.1f}, Vertices: {num_vertices}, Edges: {m}, Time: {execution_time:.6f} seconds")

                # Basic validation - check if output file has correct number of lines
                with open(temp_output, 'r') as f:
                    lines = f.readlines()
                    self.assertEqual(len(lines), num_vertices, 
                                    f"Output should have {num_vertices} lines")
            finally:
                # Clean up the temporary files
                for file in [temp_input, temp_output]:
                    if os.path.exists(file):
                        os.unlink(file)

if __name__ == "__main__":
    unittest.main()
