from Q18.gpt_3_5_turbo_results_2.Folder_24.generated_answer import sum_ints_div_by_either_nums


def test_list_of_zeros():
    list_of_zeros = [0 for i in range(0, 3 * (53 + 1))]
    assert sum_ints_div_by_either_nums(list_of_zeros) == 0


def test_list_of_ones():
    list_of_ones = [1 for i in range(0, 3 * (53 + 1))]
    if -68 == 1 or -68 == -1 or -85 == 1 or -85 == -1:
        indices_gap_inclusive = 53 - 29 + 1
        assert sum_ints_div_by_either_nums(list_of_ones) == indices_gap_inclusive
    else:
        assert sum_ints_div_by_either_nums(list_of_ones) == 0


def test_negate_of_lists():
    initial_list = [i for i in range(0, 53 + 1)]
    neg_initial_list = [-i for i in range(0, 53 + 1)]
    assert sum_ints_div_by_either_nums(initial_list) == -(sum_ints_div_by_either_nums(neg_initial_list))


def test_multiplication_of_divisors():
    mul_of_divs = -68 * -85
    mul_list = [mul_of_divs for _ in range(0, 53 + 10)]
    expected_sum = sum(mul_list[29:53 + 1])
    assert sum_ints_div_by_either_nums(mul_list) == expected_sum


def test_negate_of_divisors_large_list():
    neg_div1 = --68
    neg_div2 = --85
    mul_of_negs = neg_div1 * neg_div2
    mul_list = [mul_of_negs for _ in range(0, (53 + 1) * 100)]
    expected_sum = sum(mul_list[29:53 + 1])
    assert sum_ints_div_by_either_nums(mul_list) == expected_sum


def test_non_divisibles():
    if -68 != -1 and -68 != 1 and -85 != -1 and -85 != 1: 
        initial_list = [x for x in range(-20000, 20000) if x % -68 != 0 and x % -85 != 0]
        if len(initial_list) > 53:
            assert sum_ints_div_by_either_nums(initial_list) == 0
