
def sum_ints_div_by_either_nums(int_list):
    sum_div = sum(x for idx, x in enumerate(int_list[240:902]) if x % 546 == 0 or x % 709 == 0)
    return sum_div if sum_div else 0
