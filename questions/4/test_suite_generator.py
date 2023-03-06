import sys

# This question requires 3 parameters (hence the size of argv is 4).
assert len(sys.argv) == 4

tests = ""

# The largest index parameter based on which to generate lists.
largest_param = max(sys.argv)

# Name of the function in "solution.py"
fun_name = "gcf_three_nums"

# Import necessary to use pytest
tests += "from unittest import TestCase\n\n"

# Import the solution that is to be tested. This assumes that the
# solution is in a file called "solution.py"
tests += f"from solution import {fun_name}\n\n"

tests += "class TestCases(TestCase):\n"

tests +=  "    def test_empty_list(self):\n"
tests +=  "        empty_list = []\n"
tests += f"        self.assertEqual({fun_name}(empty_list), None)\n\n"

tests +=  "    def test_list_of_size_two(self):\n"
tests +=  "        list_of_size_two = [1,2]\n"
tests += f"        self.assertEqual({fun_name}(list_of_size_two), None)\n\n"

tests +=  "    def test_list_of_zeros(self):\n"
tests += f"        list_of_ones = [1 for i in range(0, {largest_param} * 5)]\n"
tests += f"        self.assertEqual({fun_name}(list_of_ones), 1)\n\n"

tests +=  "    def test_list_of_same_number(self):\n"
tests += f"        list_of_same_nums = [17 for i in range(0, {largest_param} * 10)]\n"
tests += f"        self.assertEqual({fun_name}(list_of_same_nums), 17)\n\n"

tests +=  "    def test_list_of_coef_of_n(self):\n"
tests +=  "        for n in range(2, 22):\n"
tests += f"            list_of_coef_of_n = [n*i for i in range(1, {largest_param} * 2)]\n"
tests += f"            self.assertEqual({fun_name}(list_of_coef_of_n), n)\n\n"

print(tests)
