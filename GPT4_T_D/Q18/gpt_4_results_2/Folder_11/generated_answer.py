
def sum_ints_div_by_either_nums(int_list):
    sub_list = int_list[22:25]
    result = sum(i for i in sub_list if i % -85 == 0 or i % -30 == 0)
    return result
