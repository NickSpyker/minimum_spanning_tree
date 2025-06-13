#!/usr/bin/env python3
import os
import subprocess
import unittest
import tempfile

class TestComplexGraphs(unittest.TestCase):
    """
    Test suite for more complex graph scenarios in the MST implementation.
    """

    @classmethod
    def setUpClass(cls):
        # Compile the program if it doesn't exist
        if not os.path.exists("mst"):
            subprocess.run(["make"], check=True)

    def test_disconnected_graph(self):
        """Test MST implementation with a disconnected graph."""
        # Create a temporary input file with a disconnected graph
        # Format: num_vertices num_edges start_vertex
        # Two separate components: (0-1-2) and (3-4)
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_in:
            tmp_in.write("5\t3\t0\n")  # 5 vertices, 3 edges, start at vertex 0
            tmp_in.write("0\t1\t10\n")  # Edge between 0-1 with weight 10
            tmp_in.write("1\t2\t20\n")  # Edge between 1-2 with weight 20
            tmp_in.write("3\t4\t30\n")  # Edge between 3-4 with weight 30 (disconnected from 0-1-2)
            temp_input = tmp_in.name

        # Create a temporary output file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_out:
            temp_output = tmp_out.name

        try:
            # Run the MST program
            result = subprocess.run(
                ["./mst", temp_input, temp_output],
                capture_output=True,
                text=True
            )

            # The program should still run but unreachable vertices will have INT_MAX as key
            # and their parent should remain -1 (which will be printed as their vertex number)
            self.assertEqual(result.returncode, 0, f"Program failed with: {result.stderr}")

            with open(temp_output, 'r') as f:
                lines = [line.strip() for line in f.readlines()]

                # Check source vertex
                self.assertEqual(lines[0], "0\tNIL", "Source vertex should have NIL parent")

                # Check vertices in the same component as source
                self.assertEqual(lines[1], "1\t0", "Vertex 1 should have vertex 0 as parent")
                self.assertEqual(lines[2], "2\t1", "Vertex 2 should have vertex 1 as parent")

                # Vertices 3 and 4 are unreachable, so they should have either:
                # 1. -1 as parent (implementation dependent)
                # 2. Some default value indicating unreachable
                # We'll accept either case
                self.assertTrue(
                    lines[3] in ["3\t-1", "3\tINF", "3\tNIL"],
                    f"Vertex 3 should have indicator of unreachable but got {lines[3]}"
                )
                self.assertTrue(
                    lines[4] in ["4\t-1", "4\tINF", "4\tNIL"],
                    f"Vertex 4 should have indicator of unreachable but got {lines[4]}"
                )
        finally:
            # Clean up the temporary files
            for file in [temp_input, temp_output]:
                if os.path.exists(file):
                    os.unlink(file)

    def test_complete_graph(self):
        """Test MST implementation with a complete graph (all vertices connected)."""
        # Create a temporary input file with a complete graph of 5 vertices
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_in:
            tmp_in.write("5\t10\t0\n")  # 5 vertices, 10 edges (complete graph), start at vertex 0

            # Add all possible edges with different weights
            edges = [
                (0, 1, 10), (0, 2, 15), (0, 3, 20), (0, 4, 25),
                (1, 2, 35), (1, 3, 40), (1, 4, 45),
                (2, 3, 50), (2, 4, 55),
                (3, 4, 60)
            ]

            for u, v, w in edges:
                tmp_in.write(f"{u}\t{v}\t{w}\n")

            temp_input = tmp_in.name

        # Create a temporary output file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_out:
            temp_output = tmp_out.name

        try:
            # Run the MST program
            result = subprocess.run(
                ["./mst", temp_input, temp_output],
                capture_output=True,
                text=True
            )

            # Check if the program ran successfully
            self.assertEqual(result.returncode, 0, f"Program failed with: {result.stderr}")

            # Read the output
            with open(temp_output, 'r') as f:
                lines = [line.strip() for line in f.readlines()]

                # Check if we have the right number of vertices
                self.assertEqual(len(lines), 5, "Output should have 5 lines")

                # Check source vertex
                self.assertEqual(lines[0], "0\tNIL", "Source vertex should have NIL parent")

                # For a complete graph with our weight pattern, the MST should form a star
                # with vertex 0 at the center
                self.assertEqual(lines[1], "1\t0", "Vertex 1 should have vertex 0 as parent")
                self.assertEqual(lines[2], "2\t0", "Vertex 2 should have vertex 0 as parent")
                self.assertEqual(lines[3], "3\t0", "Vertex 3 should have vertex 0 as parent")
                self.assertEqual(lines[4], "4\t0", "Vertex 4 should have vertex 0 as parent")
        finally:
            # Clean up the temporary files
            for file in [temp_input, temp_output]:
                if os.path.exists(file):
                    os.unlink(file)

if __name__ == "__main__":
    unittest.main()
