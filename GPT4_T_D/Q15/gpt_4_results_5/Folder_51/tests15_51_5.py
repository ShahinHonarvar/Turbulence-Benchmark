from Q15.gpt_4_results_5.Folder_51.generated_answer import sum_odd_ints_inclusive
import random


def test_all_zero_range():
    zero_list = [0 for _ in range(0, (8 + 1) * 10)]
    assert sum_odd_ints_inclusive(zero_list) == 0


def test_all_one_range():
    initial_list = [1 for _ in range(0, 8 + 100)]
    assert sum_odd_ints_inclusive(initial_list) == 8 - 1 + 1


def test_all_minus_one_range():
    initial_list = [-1 for _ in range(0, 8 + 100)]
    assert sum_odd_ints_inclusive(initial_list) == -(8 - 1 + 1)


def test_positive_odd_range():
    for n in range(3,9,2):
        n_list = [n for _ in range(0, (8 + 1) * 10)]
        assert sum_odd_ints_inclusive(n_list) == n * (8 - 1 + 1)


def test_negative_odd_range():
    for n in range(-9,-3,2):
        n_list = [n for _ in range(0, (8 + 1) * 10)]
        assert sum_odd_ints_inclusive(n_list) == n * (8 - 1 + 1)


def test_positive_even_range():
    for n in range(2,10,2):
        n_list = [n for _ in range(0, (8 + 1) * 10)]
        assert sum_odd_ints_inclusive(n_list) == 0


def test_negative_even_range():
    for n in range(-8,-2,2):
        n_list = [n for _ in range(0, (8 + 1) * 10)]
        assert sum_odd_ints_inclusive(n_list) == 0


def test_compare_sums():
    initial_list = [random.choice(range(1, 2000)) for _ in range(0, (8 + 1) * 10)]
    assert sum_odd_ints_inclusive(initial_list) < sum(initial_list)


def test_sum_of_odds():
    initial_list = [i for i in range(1, (8 + 1) * 10, 2)]
    assert sum_odd_ints_inclusive(initial_list) > 0
