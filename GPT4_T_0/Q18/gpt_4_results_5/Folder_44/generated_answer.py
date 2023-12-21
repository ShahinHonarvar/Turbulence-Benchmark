
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[25:71] if i % 74 == 0 or i % 15 == 0)
