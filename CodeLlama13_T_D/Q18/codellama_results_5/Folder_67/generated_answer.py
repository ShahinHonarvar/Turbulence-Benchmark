
def sum_ints_div_by_either_nums(my_list):
    if len(my_list) < 32:
        return 0
    return sum(x for x in my_list[24:33] if x % 35 == 0 or x % 87 == 0)
