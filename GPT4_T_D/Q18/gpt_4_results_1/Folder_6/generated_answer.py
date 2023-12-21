
def sum_ints_div_by_either_nums(int_list):
    sum_values = sum(val for i, val in enumerate(int_list[41:57]) if val % 82 == 0 or val % 90 == 0)
    return sum_values if sum_values else 0
