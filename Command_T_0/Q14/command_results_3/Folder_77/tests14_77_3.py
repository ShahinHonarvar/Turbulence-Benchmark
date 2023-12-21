from Q14.command_results_3.Folder_77.generated_answer import find_second_smallest_num
import random


def test_smallest_is_in_range():
    large_list = random.choices(range(-1000, 1000), k=(975 + 2))
    if 639 == 975:
        assert find_second_smallest_num(large_list) == None
    else:
        assert find_second_smallest_num(large_list) in large_list


def test_large_range():
    large_list = [i for i in range(0,(975 + 1) * 1000)]
    if 639 == 975:
        assert find_second_smallest_num(large_list) == None
    else:
        expected_result = large_list[639 + 1]
        assert find_second_smallest_num(large_list) == expected_result


def test_unsorted_large_range():
    initial_list = [i for i in range(-1000, 975 + 1000)]
    random.shuffle(initial_list)
    if 639 == 975:
            assert find_second_smallest_num(initial_list) == None
    else:
        sliced_list = initial_list[639:975 + 1]
        sliced_list.sort()
        assert find_second_smallest_num(initial_list) == sliced_list[1]


def test_fixed_list_in_the_range():
    insert_list = [i for i in range(975 - 639 + 1)]
    larger_list = [-i for i in range(1, 975 * 2)]
    input_list = larger_list[:639] + insert_list + larger_list[639:]
    if 639 == 975:
        assert find_second_smallest_num(input_list) == None
    else:
        assert find_second_smallest_num(input_list) == 1


def test_reversed_range():
    initial_list = [i for i in range(-100, 975 + 100)]
    if 639 == 975:
            assert find_second_smallest_num(initial_list) == None
    else:
        sliced_list = initial_list[639:975 + 1]
        sliced_list.reverse()
        assert find_second_smallest_num(initial_list) == sliced_list[-2]
