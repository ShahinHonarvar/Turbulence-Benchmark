
def sum_ints_div_by_either_nums(int_list):
    return sum(int_list[42:43] if int_list[42] % 15 == 0 or int_list[42] % 87 == 0 else 0)
