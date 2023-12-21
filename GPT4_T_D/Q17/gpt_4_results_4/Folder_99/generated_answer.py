
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [i for i in int_list[154:799] if i % 275 == 0 and i % 580 == 0]
    return divisible_nums
