from Q18.codellama_results_4.Folder_17.generated_answer import sum_ints_div_by_either_nums


def test_list_of_zeros():
    list_of_zeros = [0 for i in range(0, 3 * (89 + 1))]
    assert sum_ints_div_by_either_nums(list_of_zeros) == 0


def test_list_of_ones():
    list_of_ones = [1 for i in range(0, 3 * (89 + 1))]
    if 56 == 1 or 56 == -1 or 68 == 1 or 68 == -1:
        indices_gap_inclusive = 89 - 81 + 1
        assert sum_ints_div_by_either_nums(list_of_ones) == indices_gap_inclusive
    else:
        assert sum_ints_div_by_either_nums(list_of_ones) == 0


def test_negate_of_lists():
    initial_list = [i for i in range(0, 89 + 1)]
    neg_initial_list = [-i for i in range(0, 89 + 1)]
    assert sum_ints_div_by_either_nums(initial_list) == -(sum_ints_div_by_either_nums(neg_initial_list))


def test_multiplication_of_divisors():
    mul_of_divs = 56 * 68
    mul_list = [mul_of_divs for _ in range(0, 89 + 10)]
    expected_sum = sum(mul_list[81:89 + 1])
    assert sum_ints_div_by_either_nums(mul_list) == expected_sum


def test_negate_of_divisors_large_list():
    neg_div1 = -56
    neg_div2 = -68
    mul_of_negs = neg_div1 * neg_div2
    mul_list = [mul_of_negs for _ in range(0, (89 + 1) * 100)]
    expected_sum = sum(mul_list[81:89 + 1])
    assert sum_ints_div_by_either_nums(mul_list) == expected_sum


def test_non_divisibles():
    if 56 != -1 and 56 != 1 and 68 != -1 and 68 != 1: 
        initial_list = [x for x in range(-20000, 20000) if x % 56 != 0 and x % 68 != 0]
        if len(initial_list) > 89:
            assert sum_ints_div_by_either_nums(initial_list) == 0
