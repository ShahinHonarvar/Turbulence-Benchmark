
def sum_ints_div_by_either_nums(int_list):
    applicable_ints = int_list[57:85]
    sum_of_ints = sum(i for i in applicable_ints if i % -30 == 0 or i % -88 == 0)
    return sum_of_ints
