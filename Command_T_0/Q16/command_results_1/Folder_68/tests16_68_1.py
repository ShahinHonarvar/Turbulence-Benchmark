from Q16.command_results_1.Folder_68.generated_answer import sum_even_ints_inclusive
import random


def test_even_range():
    for n in range(-50,51,2):
        n_list = [n for _ in range(0, (8 + 1) * 10)]
        assert sum_even_ints_inclusive(n_list) == n * (8 - 0 + 1)


def test_odd_range():
    odd_list = [i for i in range(-10001,8 * 10,2)]
    assert sum_even_ints_inclusive(odd_list) == 0


def test_all_zero_range():
    zero_list = [0 for _ in range(0, (8 + 1) * 10)]
    assert sum_even_ints_inclusive(zero_list) == 0


def test_all_one_range():
    initial_list = [1 for _ in range(0, (8 + 1) * 10)]
    assert sum_even_ints_inclusive(initial_list) == 0


def test_compare_sums():
    initial_list = [random.choice(range(1, 2000)) for _ in range(0, (8 + 1) * 10)]
    assert sum_even_ints_inclusive(initial_list) < sum(initial_list)


def test_sum_of_evens():
    initial_list = [i for i in range(2, (8 + 1) * 10, 2)]
    assert sum_even_ints_inclusive(initial_list) > 0


def test_sum_by_n_times_n_plus_one():
    initial_list = [i for i in range(1, (8 + 1) * 10)]
    upper_bound = initial_list[8]
    number_of_even_with_ub  = upper_bound / 2 if upper_bound % 2 == 0 else upper_bound // 2
    lower_bound = initial_list[0] - 1
    number_of_evens_with_lb  = lower_bound / 2 if lower_bound % 2 == 0 else lower_bound // 2
    expected_result = (number_of_even_with_ub * (number_of_even_with_ub + 1)) - (number_of_evens_with_lb * (number_of_evens_with_lb + 1))
    assert sum_even_ints_inclusive(initial_list) == expected_result
    