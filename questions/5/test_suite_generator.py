import sys

# This question requires 1 parameters (hence the size of argv is 2).
assert len(sys.argv) == 2

tests = ""

# Name of the function in "solution.py"
fun_name = "find_primes"

# Import necessary to use pytest
tests += "from unittest import TestCase\n\n"

# Import the solution that is to be tested. This assumes that the
# solution is in a file called "solution.py"
tests += f"from solution import {fun_name}\n\n"

tests += "class TestCases(TestCase):\n"

tests +=  "    def test_empty_list(self):\n"
tests +=  "        empty_list = []\n"
tests += f"        self.assertEqual({fun_name}(empty_list), [])\n\n"

tests +=  "    def test_list_of_two(self):\n"
tests +=  "        list_of_two = [2]\n"
tests += f"        if {int(sys.argv[1])} < 3:\n"
tests += f"            self.assertEqual({fun_name}(list_of_two), [])\n"
tests +=  "        else:\n"
tests += f"            self.assertEqual({fun_name}(list_of_two), [2])\n\n"

tests +=  "    def test_list_of_zeros_and_ones(self):\n"
tests += f"        list_of_zeros_and_ones = [0 if i % 2 == 0 else 1 for i in range(0, 100)]\n"
tests += f"        self.assertEqual({fun_name}(list_of_zeros_and_ones), [])\n\n"

tests +=  "    def test_list_of_non_prime_nums(self):\n"
tests +=  "        for n in range(2,10):\n"
tests += f"            list_of_non_prime_nums = [n*i for i in range(2, 100)]\n"
tests += f"            self.assertEqual({fun_name}(list_of_non_prime_nums), [])\n\n"

tests +=  "    def test_list_of_negative_nums(self):\n"
tests += f"        list_of_negative_nums = [i for i in range(-1, -50, -1)]\n"
tests += f"        self.assertEqual({fun_name}(list_of_negative_nums), [])\n\n"

tests +=  "    def test_list_of_mixed_nums(self):\n"
tests += f"        list_of_mixed_nums = [i for i in range(-50, 50)]\n"
tests += f"        list_of_positive_nums = [i for i in range(2, 50)]\n"
tests += f"        self.assertEqual({fun_name}(list_of_mixed_nums), {fun_name}(list_of_positive_nums))\n\n"

print(tests)
