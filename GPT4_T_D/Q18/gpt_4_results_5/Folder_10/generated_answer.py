
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[32:100] if i%(-11) == 0 or i%(-15) == 0)
