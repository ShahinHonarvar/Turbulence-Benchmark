
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[:9] if i % -3 == 0 or i % 8 == 0)
