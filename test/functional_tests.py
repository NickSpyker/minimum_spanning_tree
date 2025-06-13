#!/usr/bin/env python3

import os
import subprocess
import glob
import filecmp
import sys

def run_test(executable, input_file, output_file, expected_output):
    """
    Run the MST program with the given input file and compare the output with the expected output.
    """
    # Run the MST program
    try:
        subprocess.run([executable, input_file, output_file], check=True)
        print(f"✓ Successfully executed: {executable} {input_file} {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error executing: {executable} {input_file} {output_file}")
        print(f"  Error: {e}")
        return False

    # Check if the output file exists
    if not os.path.exists(output_file):
        print(f"✗ Output file not created: {output_file}")
        return False

    # Read the files and normalize whitespace
    with open(output_file, 'r') as f1, open(expected_output, 'r') as f2:
        output_lines = [line.strip() for line in f1.readlines() if line.strip()]
        expected_lines = [line.strip() for line in f2.readlines() if line.strip()]
    
    # Compare the normalized content
    if output_lines == expected_lines:
        print(f"✓ Output matches expected: {output_file} == {expected_output}")
        return True
    else:
        print(f"✗ Output does not match expected: {output_file} != {expected_output}")

        # Show differences
        print(f"  Differences:")
        if len(output_lines) != len(expected_lines):
            print(f"  - Line count: {len(output_lines)} vs {len(expected_lines)} (expected)")

        for i, (line1, line2) in enumerate(zip(output_lines, expected_lines)):
            if line1 != line2:
                print(f"  - Line {i+1}: '{line1}' vs '{line2}' (expected)")

        return False

def main():
    # Check if executable exists
    if not os.path.exists('./mst'):
        print("Error: Executable './mst' not found. Please compile the program first.")
        print("Run 'make' to compile the program.")
        return 1

    # Create temporary directory for test outputs
    os.makedirs('test_outputs', exist_ok=True)

    # Get all input files
    input_files = sorted(glob.glob('data/input/input_mst_*.txt'))

    if not input_files:
        print("Error: No input files found in data/input/")
        return 1

    print(f"Found {len(input_files)} input files.")

    # Run tests for each input file
    all_passed = True
    for input_file in input_files:
        # Determine expected output file
        base_name = os.path.basename(input_file)
        output_num = base_name.replace('input_mst_', '').replace('.txt', '')
        expected_output = f"data/output/output_mst_{output_num}.txt"

        if not os.path.exists(expected_output):
            print(f"✗ Expected output file not found: {expected_output}")
            all_passed = False
            continue

        # Determine test output file
        test_output = f"test_outputs/output_mst_{output_num}.txt"

        print(f"\nTesting with {input_file}:")
        if not run_test('./mst', input_file, test_output, expected_output):
            all_passed = False

    print("\nSummary:")
    if all_passed:
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
