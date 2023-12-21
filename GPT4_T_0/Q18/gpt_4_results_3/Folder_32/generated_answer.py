
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[25:96] if i % 51 == 0 or i % 77 == 0)
