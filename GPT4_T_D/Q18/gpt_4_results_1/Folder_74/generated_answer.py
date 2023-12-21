
def sum_ints_div_by_either_nums(int_list):
    targeted_nums = int_list[90:98]
    return sum(i for i in targeted_nums if i % 13 == 0 or i % 35 == 0)
