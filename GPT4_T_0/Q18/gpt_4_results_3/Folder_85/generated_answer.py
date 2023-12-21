
def sum_ints_div_by_either_nums(int_list):
    sum_divisible = 0
    for i in range(1, 9):
        if int_list[i] % -9 == 0 or int_list[i] % -3 == 0:
            sum_divisible += int_list[i]
    return sum_divisible
