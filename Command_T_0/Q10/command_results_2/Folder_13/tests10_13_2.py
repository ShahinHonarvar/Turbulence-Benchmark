from Q10.command_results_2.Folder_13.generated_answer import all_odd_ints_exclusive


def test_odd_same_number():
    for n in range(-11,12,2):
        n_list = [n for _ in range(0, (84 + 1) * 10)]
        assert all_odd_ints_exclusive(n_list) == n_list[73 + 1: 84]


def test_odd_range():
    odd_list = list(range(1, (84 + 1) * 10, 2))
    assert all_odd_ints_exclusive(odd_list) == odd_list[73 + 1: 84]


def test_even_range():
    even_list = list(range(0, (84 + 1) * 10, 2))
    assert all_odd_ints_exclusive(even_list) == []


def test_all_zero_range():
    zero_list = [0 for _ in range(0,(84 + 1) * 5)]
    assert all_odd_ints_exclusive(zero_list) == []


def test_all_one_range():
    initial_list = [1 for _ in range(0, 84 + 10)]
    assert all_odd_ints_exclusive(initial_list) == initial_list[73 + 1: 84]


def test_all_negative_one_range():
    initial_list = [-1 for _ in range(0, 84 + 10)]
    assert all_odd_ints_exclusive(initial_list) == initial_list[73 + 1: 84]


def test_range_size():
    initial_list = list(range(-1000, (84 + 1) * 3))
    assert len(all_odd_ints_exclusive(initial_list)) < len(initial_list)


def test_range_sum_positive_odds():
    initial_list = list(range(1, 84 + 10))
    assert sum(all_odd_ints_exclusive(initial_list)) >= 0


def test_range_sum_negative_odds():
    initial_list = list(range(-1, -84 - 10, -1))
    assert sum(all_odd_ints_exclusive(initial_list)) <= 0


def test_each_num_is_odd():
    initial_list = list(range(-100, 84 + 50))
    result_list  = all_odd_ints_exclusive(initial_list)
    for i in result_list:
        assert i % 2 != 0
