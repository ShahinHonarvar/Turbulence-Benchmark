
def sum_ints_div_by_either_nums(int_list):
    sum_of_ints = 0
    for i in range(2,8):
        if int_list[i] % -1 == 0 or int_list[i] % -7 == 0:
            sum_of_ints += int_list[i]
    return sum_of_ints if sum_of_ints != 0 else 0
