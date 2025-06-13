#!/usr/bin/env python3
import os
import subprocess
import unittest
import tempfile
import filecmp
import glob

class TestMST(unittest.TestCase):
    """
    Test suite for Minimum Spanning Tree implementation.
    Tests the MST program against known input/output pairs.
    """

    @classmethod
    def setUpClass(cls):
        # Compile the program if it doesn't exist
        if not os.path.exists("mst"):
            subprocess.run(["make"], check=True)

    def test_all_input_files(self):
        """Test MST implementation against all input/output pairs in data directory."""
        # Get all input files
        input_files = sorted(glob.glob("data/input/input_mst_*.txt"))

        for input_file in input_files:
            # Derive test case number and expected output file
            test_num = os.path.basename(input_file).split('_')[-1].split('.')[0]
            expected_output = f"data/output/output_mst_{test_num}.txt"

            # Skip if expected output doesn't exist
            if not os.path.exists(expected_output):
                self.skipTest(f"No expected output for {input_file}")
                continue

            # Create a temporary output file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp:
                temp_output = tmp.name

            try:
                # Run the MST program
                result = subprocess.run(
                    ["./mst", input_file, temp_output],
                    capture_output=True,
                    text=True,
                    check=True
                )

                # Check if the output matches the expected output
                self.assertTrue(
                    filecmp.cmp(temp_output, expected_output, shallow=False),
                    f"Output for {input_file} doesn't match expected output"
                )
            finally:
                # Clean up the temporary file
                if os.path.exists(temp_output):
                    os.unlink(temp_output)

    def test_edge_case_empty_graph(self):
        """Test MST implementation with an empty graph."""
        # Create a temporary input file with an empty graph
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_in:
            tmp_in.write("0\t0\t0\n")
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

            # Check if the output file exists and is empty
            self.assertTrue(os.path.exists(temp_output))
            with open(temp_output, 'r') as f:
                content = f.read().strip()
                self.assertEqual(content, "0\tNIL", "Empty graph should produce only source vertex with NIL parent")
        finally:
            # Clean up the temporary files
            for file in [temp_input, temp_output]:
                if os.path.exists(file):
                    os.unlink(file)

    def test_single_edge_graph(self):
        """Test MST implementation with a graph containing a single edge."""
        # Create a temporary input file with a graph containing a single edge
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_in:
            tmp_in.write("2\t1\t0\n")
            tmp_in.write("0\t1\t5\n")
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

            # Check the output
            with open(temp_output, 'r') as f:
                lines = f.readlines()
                self.assertEqual(len(lines), 2, "Output should have 2 lines")
                self.assertEqual(lines[0].strip(), "0\tNIL", "First vertex should have NIL parent")
                self.assertEqual(lines[1].strip(), "1\t0", "Second vertex should have vertex 0 as parent")
        finally:
            # Clean up the temporary files
            for file in [temp_input, temp_output]:
                if os.path.exists(file):
                    os.unlink(file)

if __name__ == "__main__":
    unittest.main()
