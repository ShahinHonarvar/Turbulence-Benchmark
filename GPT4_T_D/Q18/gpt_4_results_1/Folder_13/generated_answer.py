
def sum_ints_div_by_either_nums(int_list):
    subset = int_list[13:19]
    return sum(i for i in subset if i % 20 == 0 or i % 45 == 0)
