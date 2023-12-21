
def sum_ints_div_by_either_nums(int_list):
    sub_list = int_list[72:94]
    sum_nums = sum(i for i in sub_list if i % 32 == 0 or i % 44 == 0)
    return sum_nums
