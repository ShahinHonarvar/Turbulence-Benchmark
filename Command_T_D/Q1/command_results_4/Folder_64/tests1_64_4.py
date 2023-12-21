from Q1.command_results_4.Folder_64.generated_answer import all_ints_inclusive


def test_large_range():
    large_list = list(range(0, 4 + 1000))
    expected_list = list(range(0, 4 + 1))
    assert all_ints_inclusive(large_list) == expected_list


def test_minimal_range():
    exact_list = list(range(0, 4 + 1))
    expected_list = list(range(0, 4 + 1))
    assert all_ints_inclusive(exact_list) == expected_list


def test_even_range():
    even_list = [2 * i for i in range(0, 4 + 1)]
    expected_list = [2 * i for i in range(0, 4 + 1)]
    assert all_ints_inclusive(even_list) == expected_list


def test_n_nums():
    for n in range(1,21):
        n_list = [n * i for i in range(0, 2 * (4 + 1))]
        expected_list = [n * i for i in range(0, 4 + 1)]
        assert all_ints_inclusive(n_list) == expected_list


def test_lengths():
    initial_list = [i for i in range(0, 4 + 1)]
    expected_list = all_ints_inclusive(initial_list)
    assert len(expected_list) <= len(initial_list)


def test_sums():
    initial_list = [x for x in range(0, 4 + 1)]
    expected_list = all_ints_inclusive(initial_list)
    assert sum(expected_list) <= sum(initial_list)


def test_list_concat():
    initial_list = [i for i in range(0, (4 + 1) * 10)]
    sublist_upto_first_index = initial_list[:0]
    sublist_between_indices = all_ints_inclusive(initial_list)
    sublist_from_second_index = initial_list[4 + 1:]
    assert (sublist_upto_first_index + sublist_between_indices + sublist_from_second_index) == initial_list
