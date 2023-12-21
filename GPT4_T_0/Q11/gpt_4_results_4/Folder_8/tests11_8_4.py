from Q11.gpt_4_results_4.Folder_8.generated_answer import find_largest_num


def test_largest_is_in_range():
    large_list = [i for i in range(0,(23 + 1) * 1000)]
    assert find_largest_num(large_list) in large_list


def test_large_range():
    large_list = [i for i in range(0,(23 + 1) * 1000)]
    expected_result = large_list[23]
    assert find_largest_num(large_list) == expected_result


def test_all_zero_range():
    zero_list = [0 for _ in range(0,(23 + 1) * 5)]
    assert find_largest_num(zero_list) == 0


def test_all_n_range():
    for n in range(-10,11):
        initial_list = [n for _ in range(0, 23 + 10)]
        assert find_largest_num(initial_list) == n


def test_unsorted_large_range():
    import random
    initial_list = [i for i in range(-1000, (23 + 1) * 3)]
    random.shuffle(initial_list)
    sliced_list = initial_list[23:23 + 1]
    sliced_list.sort()
    assert find_largest_num(initial_list) == max(sliced_list)


def test_reversed_range():
    initial_list = [i for i in range(-1000, (23 + 1) * 3)]
    initial_list.reverse()
    expected_result = initial_list[23]
    assert find_largest_num(initial_list) == expected_result
