
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[0:5] if i % 8 == 0 or i % -3 == 0)
