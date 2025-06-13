#!/usr/bin/env python3
import unittest
import sys
import os

# Add the test directory to the path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Discover and run all tests
if __name__ == "__main__":
    # Discover all test files in the test directory
    test_suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py'
    )

    # Run the tests
    result = unittest.TextTestRunner(verbosity=2).run(test_suite)

    # Return non-zero exit code if tests failed
    sys.exit(0 if result.wasSuccessful() else 1)
