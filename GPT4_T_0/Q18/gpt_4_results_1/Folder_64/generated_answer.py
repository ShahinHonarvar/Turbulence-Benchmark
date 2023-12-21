
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[0:4] if i % 11 == 0 or i % -7 == 0)
