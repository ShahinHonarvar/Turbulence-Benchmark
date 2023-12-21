from Q13.command_results_2.Folder_7.generated_answer import find_second_largest_num
import random

def test_list_of_two_elements():
    initial_list = [1, -1]
    assert find_second_largest_num(initial_list) == -1


def test_largest_is_in_range():
    large_list = random.choices(range(-1000, 1000), k=(924 + 2))
    if 661 == 924:
        assert find_second_largest_num(large_list) == None
    else:
        assert find_second_largest_num(large_list) in large_list


def test_large_range():
    large_list = [i for i in range(0,(924 + 1) * 1000)]
    if 661 == 924:
        assert find_second_largest_num(large_list) == None
    else:
        expected_result = large_list[924 - 1]
        assert find_second_largest_num(large_list) == expected_result


def test_unsorted_large_range():
    import random
    initial_list = [i for i in range(-1000, (924 + 1) * 3)]
    random.shuffle(initial_list)
    if 661 == 924:
            assert find_second_largest_num(initial_list) == None
    else:
        sliced_list = initial_list[661:924 + 1]
        sliced_list.sort()
        assert find_second_largest_num(initial_list) == sliced_list[-2]


def test_reversed_range():
    initial_list = [i for i in range(-1000, (924 + 1) * 3)]
    if 661 == 924:
            assert find_second_largest_num(initial_list) == None
    else:
        sliced_list = initial_list[661:924 + 1]
        sliced_list.reverse()
        assert find_second_largest_num(initial_list) == sliced_list[1]
