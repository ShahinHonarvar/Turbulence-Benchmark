import sys

# This question requires 2 parameters (hence the size of argv is 3).
assert len(sys.argv) == 3

tests = ""

# Import necessary to use pytest
tests += "from unittest import TestCase\n\n"

# Import the solution that is to be tested. This assumes that the
# solution is in a file called "solution.py"
tests += "from solution import all_ints_inclusive\n\n"

tests += "class TestCases(TestCase):\n"

tests += "    def test_large_range(self):\n"
tests += f"         large_list = list(range(0, {int(sys.argv[2]) + 1000}))\n"
tests += f"         expected_list = list(range({sys.argv[1]}, {int(sys.argv[2]) + 1}))\n"
tests += "         self.assertEquals(all_ints_inclusive(large_list), expected_list)\n\n"

tests += "    def test_minimal_range(self):\n"
tests += f"         exact_list = list(range(0, {int(sys.argv[2]) + 1}))\n"
tests += f"         expected_list = list(range({sys.argv[1]}, {int(sys.argv[2]) + 1}))\n"
tests += "         self.assertEquals(all_ints_inclusive(exact_list), expected_list)\n\n"

tests += "    def test_even_range(self):\n"
tests += f"         even_list = [2 * x for x in range(0, {int(sys.argv[2]) + 1})]\n"
tests += f"         expected_list = [2 * x for x in range({sys.argv[1]}, {int(sys.argv[2]) + 1})]\n"
tests += "         self.assertEquals(all_ints_inclusive(even_list), expected_list)\n\n"

tests += "    def test_zeros(self):\n"
tests += f"         zeros_list = [0 for x in range(0, {2 * int(sys.argv[2]) + 1})]\n"
tests += f"         expected_list = [0 for x in range({sys.argv[1]}, {int(sys.argv[2]) + 1})]\n"
tests += "         self.assertEquals(all_ints_inclusive(zeros_list), expected_list)\n\n"

print(tests)
