
def sum_ints_div_by_either_nums(int_list):
    sum_val = 0
    for i in range(55, 81):
        if i < len(int_list):
            if int_list[i] % 22 == 0 or int_list[i] % 32 == 0:
                sum_val += int_list[i]
    return sum_val
