
def sum_ints_div_by_either_nums(int_list):
    return sum(i for i in int_list[3:10] if i % 6 == 0 or i % 1 == 0)
