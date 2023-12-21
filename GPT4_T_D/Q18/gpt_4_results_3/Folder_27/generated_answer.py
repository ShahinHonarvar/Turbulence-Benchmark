
def sum_ints_div_by_either_nums(int_list):
    subset = int_list[20:36]
    return sum(i for i in subset if i % -36 == 0 or i % -89 == 0)
