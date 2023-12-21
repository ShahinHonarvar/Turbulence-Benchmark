from Q18.codellama_7b_results_3.Folder_48.generated_answer import sum_ints_div_by_either_nums


def test_list_of_zeros():
    list_of_zeros = [0 for i in range(0, 3 * (957 + 1))]
    assert sum_ints_div_by_either_nums(list_of_zeros) == 0


def test_list_of_ones():
    list_of_ones = [1 for i in range(0, 3 * (957 + 1))]
    if 982 == 1 or 982 == -1 or 319 == 1 or 319 == -1:
        indices_gap_inclusive = 957 - 306 + 1
        assert sum_ints_div_by_either_nums(list_of_ones) == indices_gap_inclusive
    else:
        assert sum_ints_div_by_either_nums(list_of_ones) == 0


def test_negate_of_lists():
    initial_list = [i for i in range(0, 957 + 1)]
    neg_initial_list = [-i for i in range(0, 957 + 1)]
    assert sum_ints_div_by_either_nums(initial_list) == -(sum_ints_div_by_either_nums(neg_initial_list))


def test_multiplication_of_divisors():
    mul_of_divs = 982 * 319
    mul_list = [mul_of_divs for _ in range(0, 957 + 10)]
    expected_sum = sum(mul_list[306:957 + 1])
    assert sum_ints_div_by_either_nums(mul_list) == expected_sum


def test_negate_of_divisors_large_list():
    neg_div1 = -982
    neg_div2 = -319
    mul_of_negs = neg_div1 * neg_div2
    mul_list = [mul_of_negs for _ in range(0, (957 + 1) * 100)]
    expected_sum = sum(mul_list[306:957 + 1])
    assert sum_ints_div_by_either_nums(mul_list) == expected_sum


def test_non_divisibles():
    if 982 != -1 and 982 != 1 and 319 != -1 and 319 != 1: 
        initial_list = [x for x in range(-20000, 20000) if x % 982 != 0 and x % 319 != 0]
        if len(initial_list) > 957:
            assert sum_ints_div_by_either_nums(initial_list) == 0
