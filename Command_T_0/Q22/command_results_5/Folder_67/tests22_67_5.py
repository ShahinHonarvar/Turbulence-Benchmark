from Q22.command_results_5.Folder_67.generated_answer import find_sum_of_multiples
import random

def test_one():
    given_number = 1
    expected_result = (42 * (42 + 1)) / 2
    assert find_sum_of_multiples(given_number) == expected_result


def test_sum_is_divisible_by_n_1():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) % n == 0


def test_sum_is_divisable_by_n_2():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) / n == (42 * (42 + 1)) / 2


def test_sum_is_divisable_by_42():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) / 42 == (n * (42 + 1)) / 2


def test_sum_of_evens_is_even():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) % 2 == 0


def test_sum():
   s = sum(range(1, 42+1))
   n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) == s * n


def test_sum_is_greator_than_n():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) > n
