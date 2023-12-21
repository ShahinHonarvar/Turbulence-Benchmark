from Q42.codellama_results_2.Folder_82.generated_answer import prime_factors
from itertools import combinations


def test_list_of_primes():
    for n in [2, 3, 5, 7, 11, 13, 17]:
        list_of_primes = [n for _ in range((83 + 1) * 10)]
        assert prime_factors(list_of_primes) == {n}


def test_list_of_ones():
    list_of_ones = [1] * (83 + 100)
    assert prime_factors(list_of_ones) == set()


def test_list_of_tens():
    list_of_tens = [10] * (83 + 100)
    assert prime_factors(list_of_tens) == {2,5}


def test_prime_factors_are_odd():
    initial_list = [i for i in range(2, (83 + 2) * 2)]
    result = prime_factors(initial_list)
    for i in result:
        if i != 2:
            assert i % 2
        else:
            assert not i % 2


def test_prime_factors():
    nums = [2, 3, 5, 7, 11]
    l = list(combinations(nums, 2))
    for i, j in l:
        initial_list = [i * j * k for k in range(1, (83 + 1) * 2)]
        assert (i in prime_factors(initial_list)) and (j in prime_factors(initial_list))


def test_powers_of_two():
    initial_list = [i**2 for i in range(1, (83 + 1) * 2)]
    assert prime_factors(initial_list) == {2}