from Q43.gpt_4_results_4.Folder_78.generated_answer import find_primes_between_indices
import random


def test_list_of_primes():
    for n in [2, 3, 5, 7, 11, 13, 17]:
        list_of_primes = [n for _ in range(83 * 10)]
        expected_result = list_of_primes[28:83 + 1]
        assert find_primes_between_indices(list_of_primes) == expected_result


def test_list_of_zeros_and_ones():
    list_of_zeros_and_ones = [0 if i % 2 == 0 else 1 for i in range(0, 100)]
    assert not find_primes_between_indices(list_of_zeros_and_ones)


def test_list_of_non_prime_nums():
    for n in range(2,10):
        list_of_non_prime_nums = [n*i for i in range(2, (83 + 1) * 10)]
        assert not find_primes_between_indices(list_of_non_prime_nums)


def test_list_of_negative_nums():
    list_of_negative_nums = [i for i in range(-1, -(83 + 1) * 10, -1)]
    assert not find_primes_between_indices(list_of_negative_nums)


def test_prime_nums_are_odd():
    initial_list = [i for i in range(1, (83 + 1) * 10)]
    prime_nums = find_primes_between_indices(initial_list)
    for prime in prime_nums:
        if prime != 2:
            assert prime % 2
        else:
            assert not prime % 2


def test_result_order():
    if 28 == 83:
        initial_list = [i for i in range(1, (83 + 1) * 10)]
        initial_list[28] = 2
        assert find_primes_between_indices(initial_list) == [2]
    else:
        length = 83 - 28 + 1
        prefix = random.choices(range(1, 1000), k=28)
        middle0 = [2] * (length - 1)
        middle1 = [3]
        suffix = random.choices(range(1, 1000), k=10)
        initial_list = prefix + middle0 + middle1 + suffix
        if "ascending" == "descending":
            assert find_primes_between_indices(initial_list) == middle1 + middle0
        else:
            assert find_primes_between_indices(initial_list) == middle0 + middle1
            