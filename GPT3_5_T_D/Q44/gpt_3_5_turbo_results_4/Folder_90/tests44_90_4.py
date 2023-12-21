from Q44.gpt_3_5_turbo_results_4.Folder_90.generated_answer import composite_nums_between_indices


def test_list_of_primes():
    for n in [2, 3, 5, 7, 11, 13, 17]:
        list_of_primes = [n for _ in range(368 * 10)]
        assert composite_nums_between_indices(list_of_primes) == set()


def test_list_of_ones():
    list_of_ones = [1 if i % 2 == 0 else 1 for i in range(368 + 100)]
    assert composite_nums_between_indices(list_of_ones) == set()


def test_list_of_non_prime_nums():
    for n in range(2,10):
        list_of_non_prime_nums = [n*i for i in range(2, (368 + 1) * 10)]
        expected_result = list_of_non_prime_nums[333:368 + 1]
        assert composite_nums_between_indices(list_of_non_prime_nums) == set(expected_result)


def test_sum_of_composites():
    initial_list = [i for i in range(368 * 10)]
    assert sum(composite_nums_between_indices(initial_list)) <= sum(initial_list)


def test_each_number_is_composite():
    initial_list = [i for i in range(368 * 10)]
    result = composite_nums_between_indices(initial_list)

    def number_of_factors(x):
        c = 0
        for i in range(1, x + 1):
            if x % i == 0:
                c += 1
        return c
    
    for i in result:
        assert number_of_factors(i) > 2
    
