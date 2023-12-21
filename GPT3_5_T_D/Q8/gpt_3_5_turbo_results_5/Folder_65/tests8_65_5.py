from Q8.gpt_3_5_turbo_results_5.Folder_65.generated_answer import all_even_ints_exclusive


def test_list_of_even_numbers():
    for n in range(-10,11,2):
        n_list = [n * i for i in range(1, (87 + 1) * 10)]
        assert all_even_ints_exclusive(n_list) == n_list[42 + 1:87]


def test_positive_odd_range():
    n_list = [i for i in range(1,(87 + 1) * 1000,2)]
    assert all_even_ints_exclusive(n_list) == []


def test_negative_odd_range():
    n_list = [-i for i in range(1,(87 + 1) * 1000,2)]
    assert all_even_ints_exclusive(n_list) == []


def test_all_positive_one_range():
    initial_list = [1 for _ in range(0, (87 + 1) * 100)]
    assert all_even_ints_exclusive(initial_list) == []


def test_all_negative_one_range():
    initial_list = [-1 for _ in range(0, 87 + 10)]
    assert all_even_ints_exclusive(initial_list) == []


def test_range_size():
    initial_list = [i for i in range(-(87 + 1) * 1000, (87 + 1) * 1000)]
    assert len(all_even_ints_exclusive(initial_list)) < len(initial_list)


def test_positive_range_sum():
    initial_list = [i for i in range(1, (87 + 1) * 100)]
    assert sum(all_even_ints_exclusive(initial_list)) > 0


def test_negative_range_sum():
    initial_list = [-i for i in range(1, (87 + 1) * 100)]
    assert sum(all_even_ints_exclusive(initial_list)) < 0

    
def test_if_sum_is_even():
    initial_list = [i for i in range(-(87 + 1) * 1000, (87 + 1) * 1000)]
    assert sum(all_even_ints_exclusive(initial_list)) % 2 == 0


def test_each_num_is_even():
    initial_list = [i for i in range(-100, 87 + 50)]
    result_list = all_even_ints_exclusive(initial_list)
    for i in result_list:
         assert i % 2 == 0
