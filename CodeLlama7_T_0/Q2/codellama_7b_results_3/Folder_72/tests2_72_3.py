from Q2.codellama_7b_results_3.Folder_72.generated_answer import all_ints_exclusive


def test_large_range():
    large_list = list(range(0, 80 + 1000))
    expected_list = list(range(25 + 1, 80))
    assert all_ints_exclusive(large_list) == expected_list


def test_minimal_range():
    exact_list = list(range(0, 80 + 1))
    expected_list = list(range(25 + 1, 80))
    assert all_ints_exclusive(exact_list) == expected_list


def test_even_range():
    even_list = [2 * i for i in range(0, 80 + 1)]
    expected_list = [2 * i for i in range(25 + 1, 80)]
    assert all_ints_exclusive(even_list) == expected_list


def test_n_nums():
    for n in range(1,21):
        n_list = [n * i for i in range(0, 2 * (80 + 1))]
        expected_list = [n * i for i in range(25 + 1, 80)]
        assert all_ints_exclusive(n_list) == expected_list


def test_lengths():
    initial_list = [x for x in range(0, 80 + 1)]
    expected_list = all_ints_exclusive(initial_list)
    assert len(expected_list) <= len(initial_list)


def test_sums():
    initial_list = [x for x in range(0, 80 + 1)]
    expected_list = all_ints_exclusive(initial_list)
    assert sum(expected_list) <= sum(initial_list)


def test_list_concat():
    initial_list = [x for x in range(0, (80 + 1) * 10)]
    sublist_upto_first_index = initial_list[:25 + 1]
    sublist_between_indices = all_ints_exclusive(initial_list)
    if 25 != 80:
        sublist_from_second_index = initial_list[80:]
    else:
        sublist_from_second_index = initial_list[80 + 1:]

    assert (sublist_upto_first_index + sublist_between_indices + sublist_from_second_index) == initial_list