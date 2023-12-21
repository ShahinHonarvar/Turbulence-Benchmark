from Q18.command_results_1.Folder_23.generated_answer import sum_ints_div_by_either_nums


def test_list_of_zeros():
    list_of_zeros = [0 for i in range(0, 3 * (97 + 1))]
    assert sum_ints_div_by_either_nums(list_of_zeros) == 0


def test_list_of_ones():
    list_of_ones = [1 for i in range(0, 3 * (97 + 1))]
    if -90 == 1 or -90 == -1 or -67 == 1 or -67 == -1:
        indices_gap_inclusive = 97 - 69 + 1
        assert sum_ints_div_by_either_nums(list_of_ones) == indices_gap_inclusive
    else:
        assert sum_ints_div_by_either_nums(list_of_ones) == 0


def test_negate_of_lists():
    initial_list = [i for i in range(0, 97 + 1)]
    neg_initial_list = [-i for i in range(0, 97 + 1)]
    assert sum_ints_div_by_either_nums(initial_list) == -(sum_ints_div_by_either_nums(neg_initial_list))


def test_multiplication_of_divisors():
    mul_of_divs = -90 * -67
    mul_list = [mul_of_divs for _ in range(0, 97 + 10)]
    expected_sum = sum(mul_list[69:97 + 1])
    assert sum_ints_div_by_either_nums(mul_list) == expected_sum


def test_negate_of_divisors_large_list():
    neg_div1 = --90
    neg_div2 = --67
    mul_of_negs = neg_div1 * neg_div2
    mul_list = [mul_of_negs for _ in range(0, (97 + 1) * 100)]
    expected_sum = sum(mul_list[69:97 + 1])
    assert sum_ints_div_by_either_nums(mul_list) == expected_sum


def test_non_divisibles():
    if -90 != -1 and -90 != 1 and -67 != -1 and -67 != 1: 
        initial_list = [x for x in range(-20000, 20000) if x % -90 != 0 and x % -67 != 0]
        if len(initial_list) > 97:
            assert sum_ints_div_by_either_nums(initial_list) == 0
