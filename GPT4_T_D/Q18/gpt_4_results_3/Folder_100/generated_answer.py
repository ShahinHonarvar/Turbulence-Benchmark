
def sum_ints_div_by_either_nums(int_list):
    subset = int_list[72:94]
    sum_values = sum(i for i in subset if i % 32 == 0 or i % 44 == 0)
    return sum_values
