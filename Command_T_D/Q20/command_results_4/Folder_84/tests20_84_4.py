from Q20.command_results_4.Folder_84.generated_answer import find_n_th_smallest_num
import random
import math


def test_n_th_smallest_is_in_range():
    large_list = [i for i in range(0,(88 + 1) * 1000)]
    assert find_n_th_smallest_num(large_list) in large_list


def test_large_range():
    large_list = [i for i in range(0,(88 + 1) * 1000)]
    expected_result = large_list[61:88 + 1][7 - 1]
    assert find_n_th_smallest_num(large_list) == expected_result


def test_unsorted_large_range():
    initial_list = [i for i in range(-1000, 88 + 1000)]
    random.shuffle(initial_list)
    sliced_list = initial_list[61:88 + 1]
    sliced_list.sort()
    assert find_n_th_smallest_num(initial_list) == sliced_list[7 - 1]


def test_reversed_range():
    initial_list = [i for i in range(-100, 88 + 100)]
    sliced_list = initial_list[61:88 + 1]
    sliced_list.reverse()
    assert find_n_th_smallest_num(initial_list) == sliced_list[-7]


def test_float_numbers():
    initial_list = [math.sqrt(i) for i in range(1, 88 + 10)]
    expected_result = initial_list[61:88 + 1][7 - 1]
    assert find_n_th_smallest_num(initial_list) == expected_result


def test_unsorted_float_numbers():
    initial_list = [math.sqrt(i) for i in range(1, 88 + 10)]
    random.shuffle(initial_list)
    sliced_list = initial_list[61:88 + 1]
    sliced_list.sort()
    assert find_n_th_smallest_num(initial_list) == sliced_list[7 - 1]

