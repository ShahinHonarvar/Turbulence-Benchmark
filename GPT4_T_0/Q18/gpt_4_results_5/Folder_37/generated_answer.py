
def sum_ints_div_by_either_nums(int_list):
    sum_divisible = 0
    for i in range(2, 8):
        if int_list[i] % -1 == 0 or int_list[i] % -7 == 0:
            sum_divisible += int_list[i]
    return sum_divisible if sum_divisible != 0 else 0
