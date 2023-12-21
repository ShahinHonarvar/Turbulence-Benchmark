
def sum_ints_div_by_either_nums(int_list):
    sum_vals = 0
    for i in range(50, 93):
        if i < len(int_list) and (int_list[i] % -94 == 0 or int_list[i] % -95 == 0):
            sum_vals += int_list[i]
    return sum_vals
