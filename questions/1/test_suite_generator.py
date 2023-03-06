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

tests +=  "    def test_large_range(self):\n"
tests += f"        large_list = list(range(0, {sys.argv[2]} + 1000))\n"
tests += f"        expected_list = list(range({sys.argv[1]}, {sys.argv[2]} + 1))\n"
tests +=  "        self.assertEquals(all_ints_inclusive(large_list), expected_list)\n\n"

tests +=  "    def test_minimal_range(self):\n"
tests += f"        exact_list = list(range(0, {sys.argv[2]} + 1))\n"
tests += f"        expected_list = list(range({sys.argv[1]}, {sys.argv[2]} + 1))\n"
tests +=  "        self.assertEquals(all_ints_inclusive(exact_list), expected_list)\n\n"

tests +=  "    def test_even_range(self):\n"
tests += f"        even_list = [2 * x for x in range(0, {sys.argv[2]} + 1)]\n"
tests += f"        expected_list = [2 * x for x in range({sys.argv[1]}, {sys.argv[2]} + 1)]\n"
tests +=  "        self.assertEquals(all_ints_inclusive(even_list), expected_list)\n\n"

tests +=  "    def test_n_nums(self):\n"
tests += f"        for n in range(1,21):\n"
tests += f"            n_list = [n * x for x in range(0, 2 * {sys.argv[2]} + 1)]\n"
tests += f"            expected_list = [n * x for x in range({sys.argv[1]}, {sys.argv[2]} + 1)]\n"
tests += f"            self.assertEquals(all_ints_inclusive(n_list), expected_list)\n\n"

tests +=  "    def test_lengths(self):\n"
tests += f"        initial_list = [x for x in range(0, {sys.argv[2]} + 1)]\n"
tests += f"        expected_list = all_ints_inclusive(initial_list)\n"
tests +=  "        self.assertEquals(len(expected_list) <= len(initial_list), True)\n\n"

tests +=  "    def test_sums(self):\n"
tests += f"        initial_list = [x for x in range(0, {sys.argv[2]} + 1)]\n"
tests += f"        expected_list = all_ints_inclusive(initial_list)\n"
tests +=  "        self.assertEquals(sum(expected_list) <= sum(initial_list), True)\n\n"

tests +=  "    def test_list_concat(self):\n"
tests += f"        initial_list = [x for x in range(0, {sys.argv[2]} * 10)]\n"
tests += f"        sublist_upto_first_index = initial_list[:{sys.argv[1]}]\n"
tests += f"        sublist_between_indices = all_ints_inclusive(initial_list)\n"
tests += f"        sublist_from_second_index = initial_list[{sys.argv[2]} + 1:]\n"
tests +=  "        self.assertEquals(sublist_upto_first_index + sublist_between_indices + sublist_from_second_index, initial_list)\n\n"


print(tests)