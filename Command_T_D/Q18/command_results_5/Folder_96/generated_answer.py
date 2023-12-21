
def sum_ints_div_by_either_nums(int_list):
    return sum(x for x in int_list[50:200] if x % -34 == 0 or x % 64 == 0)
