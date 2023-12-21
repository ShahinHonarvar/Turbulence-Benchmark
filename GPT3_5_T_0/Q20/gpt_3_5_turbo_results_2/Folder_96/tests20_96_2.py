from Q20.gpt_3_5_turbo_results_2.Folder_96.generated_answer import find_n_th_smallest_num
import random
import math


def test_n_th_smallest_is_in_range():
    large_list = [i for i in range(0,(17 + 1) * 1000)]
    assert find_n_th_smallest_num(large_list) in large_list


def test_large_range():
    large_list = [i for i in range(0,(17 + 1) * 1000)]
    expected_result = large_list[0:17 + 1][18 - 1]
    assert find_n_th_smallest_num(large_list) == expected_result


def test_unsorted_large_range():
    initial_list = [i for i in range(-1000, 17 + 1000)]
    random.shuffle(initial_list)
    sliced_list = initial_list[0:17 + 1]
    sliced_list.sort()
    assert find_n_th_smallest_num(initial_list) == sliced_list[18 - 1]


def test_reversed_range():
    initial_list = [i for i in range(-100, 17 + 100)]
    sliced_list = initial_list[0:17 + 1]
    sliced_list.reverse()
    assert find_n_th_smallest_num(initial_list) == sliced_list[-18]


def test_float_numbers():
    initial_list = [math.sqrt(i) for i in range(1, 17 + 10)]
    expected_result = initial_list[0:17 + 1][18 - 1]
    assert find_n_th_smallest_num(initial_list) == expected_result


def test_unsorted_float_numbers():
    initial_list = [math.sqrt(i) for i in range(1, 17 + 10)]
    random.shuffle(initial_list)
    sliced_list = initial_list[0:17 + 1]
    sliced_list.sort()
    assert find_n_th_smallest_num(initial_list) == sliced_list[18 - 1]

