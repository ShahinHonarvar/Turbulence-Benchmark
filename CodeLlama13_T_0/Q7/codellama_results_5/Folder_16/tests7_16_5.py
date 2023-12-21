from Q7.codellama_results_5.Folder_16.generated_answer import all_even_ints_inclusive


def test_even_n_range():
    n_list = [i for i in range(2, (36 + 10) * 2, 2)]
    assert all_even_ints_inclusive(n_list) == n_list[33:36 + 1]


def test_positive_odd_range():
    n_list = [i for i in range(1,(36 + 1) * 1000,2)]
    assert all_even_ints_inclusive(n_list) == []


def test_negative_odd_range():
    n_list = [-i for i in range(1,(36 + 1) * 1000,2)]
    assert all_even_ints_inclusive(n_list) == []


def test_all_positive_one_range():
    initial_list = [1 for _ in range(0, (36 + 1) * 100)]
    assert all_even_ints_inclusive(initial_list) == []


def test_all_negative_one_range():
    initial_list = [-1 for _ in range(0, 36 + 10)]
    assert all_even_ints_inclusive(initial_list) == []


def test_range_size():
    initial_list = [i for i in range(-(36 + 1) * 1000, (36 + 1) * 1000)]
    assert len(all_even_ints_inclusive(initial_list)) < len(initial_list)


def test_positive_range_sum():
    initial_list = [i for i in range(2, (36 + 1) * 100, 2)]
    assert sum(all_even_ints_inclusive(initial_list)) > 0


def test_negative_range_sum():
    initial_list = [-i for i in range(2, (36 + 1) * 100, 2)]
    assert sum(all_even_ints_inclusive(initial_list)) < 0


def test_if_sum_is_even():
    initial_list = [i for i in range(-(36 + 1) * 1000, (36 + 1) * 1000)]
    assert sum(all_even_ints_inclusive(initial_list)) % 2 == 0


def test_each_num_is_even():
    initial_list = [i for i in range(-100, 36 + 50)]
    result_list  = all_even_ints_inclusive(initial_list)
    for i in result_list:
        assert i % 2 == 0
    