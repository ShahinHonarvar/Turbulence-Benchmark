
def sum_ints_div_by_either_nums(int_list):
    sum_ints = 0
    for i in range(48, min(60, len(int_list))):
        if int_list[i] % 88 == 0 or int_list[i] % 58 == 0:
            sum_ints += int_list[i]
    return sum_ints
