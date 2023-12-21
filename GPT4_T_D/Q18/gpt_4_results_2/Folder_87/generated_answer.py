
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[18:53] if i % 15 == 0 or i % 57 == 0)
