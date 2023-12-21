
def sum_ints_div_by_either_nums(int_list):
    return sum(int(x) for x in int_list[10:28] if x % -61 == 0 or x % -64 == 0)
