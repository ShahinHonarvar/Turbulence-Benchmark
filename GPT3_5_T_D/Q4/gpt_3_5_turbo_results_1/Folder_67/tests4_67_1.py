from Q4.gpt_3_5_turbo_results_1.Folder_67.generated_answer import all_pos_ints_exclusive


def test_large_range():
    large_list = list(range(1, 74 + 1000))
    expected_list = large_list[49 + 1:74]
    assert all_pos_ints_exclusive(large_list) == expected_list


def test_minimal_range():
    minimal_list = list(range(1, 74 + 2))
    expected_list = minimal_list[49 + 1:74]
    assert all_pos_ints_exclusive(minimal_list) == expected_list


def test_even_range():
    even_list = [2 * i for i in range(1, 74 + 2)]
    expected_list = even_list[49 + 1:74]
    assert all_pos_ints_exclusive(even_list) == expected_list


def test_negative_range():
    neg_list = [i for i in range(0, -74 - 2, -1)]
    assert all_pos_ints_exclusive(neg_list) == []


def test_zero_range():
    zero_list = [0 for i in range(0, (74 + 2) * 10)]
    assert all_pos_ints_exclusive(zero_list) == []


def test_range_size():
    initial_list = [i for i in range(-100, 74 + 10)]
    assert len(all_pos_ints_exclusive(initial_list)) < len(initial_list)


def test_range_sum():
    initial_list = [i for i in range(0, 74 + 10)]
    assert sum(all_pos_ints_exclusive(initial_list)) >= 0 


def test_ones_range_sum():
    ones_list = [1 for i in range(0, 74 + 1)]
    if 49 != 74:
        assert sum(all_pos_ints_exclusive(ones_list)) == 74 - 49 - 1
    else:
        assert sum(all_pos_ints_exclusive(ones_list)) == 0