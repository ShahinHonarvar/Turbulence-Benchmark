from Q14.gpt_4_results_4.Folder_16.generated_answer import find_second_smallest_num
import random


def test_smallest_is_in_range():
    large_list = random.choices(range(-1000, 1000), k=(77 + 2))
    if 66 == 77:
        assert find_second_smallest_num(large_list) == None
    else:
        assert find_second_smallest_num(large_list) in large_list


def test_large_range():
    large_list = [i for i in range(0,(77 + 1) * 1000)]
    if 66 == 77:
        assert find_second_smallest_num(large_list) == None
    else:
        expected_result = large_list[66 + 1]
        assert find_second_smallest_num(large_list) == expected_result


def test_unsorted_large_range():
    initial_list = [i for i in range(-1000, 77 + 1000)]
    random.shuffle(initial_list)
    if 66 == 77:
            assert find_second_smallest_num(initial_list) == None
    else:
        sliced_list = initial_list[66:77 + 1]
        sliced_list.sort()
        assert find_second_smallest_num(initial_list) == sliced_list[1]


def test_fixed_list_in_the_range():
    insert_list = [i for i in range(77 - 66 + 1)]
    larger_list = [-i for i in range(1, 77 * 2)]
    input_list = larger_list[:66] + insert_list + larger_list[66:]
    if 66 == 77:
        assert find_second_smallest_num(input_list) == None
    else:
        assert find_second_smallest_num(input_list) == 1


def test_reversed_range():
    initial_list = [i for i in range(-100, 77 + 100)]
    if 66 == 77:
            assert find_second_smallest_num(initial_list) == None
    else:
        sliced_list = initial_list[66:77 + 1]
        sliced_list.reverse()
        assert find_second_smallest_num(initial_list) == sliced_list[-2]
