
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[0:6] if i % -1 == 0 or i % 13 == 0)
