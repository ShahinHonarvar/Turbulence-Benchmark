from Q14.codellama_7b_results_2.Folder_38.generated_answer import find_second_smallest_num
import random


def test_smallest_is_in_range():
    large_list = random.choices(range(-1000, 1000), k=(51 + 2))
    if 37 == 51:
        assert find_second_smallest_num(large_list) == None
    else:
        assert find_second_smallest_num(large_list) in large_list


def test_large_range():
    large_list = [i for i in range(0,(51 + 1) * 1000)]
    if 37 == 51:
        assert find_second_smallest_num(large_list) == None
    else:
        expected_result = large_list[37 + 1]
        assert find_second_smallest_num(large_list) == expected_result


def test_unsorted_large_range():
    initial_list = [i for i in range(-1000, 51 + 1000)]
    random.shuffle(initial_list)
    if 37 == 51:
            assert find_second_smallest_num(initial_list) == None
    else:
        sliced_list = initial_list[37:51 + 1]
        sliced_list.sort()
        assert find_second_smallest_num(initial_list) == sliced_list[1]


def test_fixed_list_in_the_range():
    insert_list = [i for i in range(51 - 37 + 1)]
    larger_list = [-i for i in range(1, 51 * 2)]
    input_list = larger_list[:37] + insert_list + larger_list[37:]
    if 37 == 51:
        assert find_second_smallest_num(input_list) == None
    else:
        assert find_second_smallest_num(input_list) == 1


def test_reversed_range():
    initial_list = [i for i in range(-100, 51 + 100)]
    if 37 == 51:
            assert find_second_smallest_num(initial_list) == None
    else:
        sliced_list = initial_list[37:51 + 1]
        sliced_list.reverse()
        assert find_second_smallest_num(initial_list) == sliced_list[-2]
