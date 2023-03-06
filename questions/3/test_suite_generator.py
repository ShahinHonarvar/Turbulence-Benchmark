import sys

# This question requires 4 parameters (hence the size of argv is 5).
assert len(sys.argv) == 5

tests = ""

# Name of the function in "solution.py"
fun_name = "sum_ints_div_by_nums"

# Import necessary to use pytest
tests += "from unittest import TestCase\n\n"

# Import the solution that is to be tested. This assumes that the
# solution is in a file called "solution.py"
tests += f"from solution import {fun_name}\n\n"

tests += "class TestCases(TestCase):\n"

tests +=  "    def test_empty_list(self):\n"
tests +=  "        empty_list = []\n"
tests += f"        self.assertEqual({fun_name}(empty_list), 0)\n\n"

tests +=  "    def test_list_of_zeros(self):\n"
tests += f"        list_of_zeros = [0 for i in range(0, {3 * int(sys.argv[4]) + 1})]\n"
tests += f"        self.assertEqual({fun_name}(list_of_zeros), 0)\n\n"

tests +=  "    def test_negate_of_lists(self):\n"
tests += f"        initial_list = [i for i in range(0, {int(sys.argv[4]) + 1})]\n"
tests += f"        neg_initial_list = [-i for i in range(0, {int(sys.argv[4]) + 1})]\n"
tests += f"        self.assertEqual({fun_name}(initial_list), -({fun_name}(neg_initial_list)))\n\n"

tests +=  "    def test_multiplication_of_divisors(self):\n"
tests += f"        mul_of_divs = {int(sys.argv[1])} * {int(sys.argv[2])}\n"
tests += f"        mul_list = [mul_of_divs for _ in range(0, {int(sys.argv[4])} + 10)]\n"
tests += f"        expected_sum = sum(mul_list[{int(sys.argv[3])}:{int(sys.argv[4])}+1])\n"
tests += f"        self.assertEqual({fun_name}(mul_list), expected_sum)\n\n"

tests +=  "    def test_negate_of_divisors_large_list(self):\n"
tests += f"        neg_div1 = -{int(sys.argv[1])}\n"
tests += f"        neg_div2 = -{int(sys.argv[2])}\n"
tests +=  "        mul_of_negs = neg_div1 * neg_div2\n"
tests += f"        mul_list = [mul_of_negs for _ in range(0, {int(sys.argv[4])} * 100)]\n"
tests += f"        expected_sum = sum(mul_list[{int(sys.argv[3])}:{int(sys.argv[4])}+1])\n"
tests += f"        self.assertEqual({fun_name}(mul_list), expected_sum)\n\n"

print(tests)
