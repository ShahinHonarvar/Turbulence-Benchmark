from Q19.codellama_results_3.Folder_84.generated_answer import all_ints_not_div_by_num


def test_list_of_zeros():
    list_of_zeros = [0 for i in range(0, 3 * (81 + 1))]
    assert all_ints_not_div_by_num(list_of_zeros) == []


def test_negate_of_lists():
    initial_list = [i for i in range(0, 81 + 1)]
    neg_initial_list = [-i for i in range(0, 81 + 1)]
    expected_list = [-i for i in all_ints_not_div_by_num(neg_initial_list)]
    assert all_ints_not_div_by_num(initial_list) == expected_list


def test_negate_of_divisors():
    neg_div = -64
    neg_div_list = [neg_div for _ in range(0, 81 + 1)]
    assert all_ints_not_div_by_num(neg_div_list) == []


def test_compare_neg_divisor():
    initial_list = [i for i in range(0, 81 + 1)]
    neg_div = -64
    neg_div_result_list = [i for i in initial_list[50 + 1: 81] if i % neg_div != 0]
    assert all_ints_not_div_by_num(initial_list) == neg_div_result_list


def test_lengths():
    initial_list = [x for x in range(0, 81 + 1)]
    expected_list = all_ints_not_div_by_num(initial_list)
    assert len(expected_list) <= len(initial_list)


def test_sums():
    initial_list = [x for x in range(0, 81 + 1)]
    expected_list = all_ints_not_div_by_num(initial_list)
    assert sum(expected_list) <= sum(initial_list)


def test_coefficient_of_divisor():
    for n in range(-10,11):
        initial_list = [64 * n for _ in range(0, 81 + 1)]
        assert all_ints_not_div_by_num(initial_list) == []
        

def test_divisibles():
    initial_list = [x for x in range(-20000, 20000) if x % 64 == 0]
    if len(initial_list) > 81:
        assert all_ints_not_div_by_num(initial_list) == []