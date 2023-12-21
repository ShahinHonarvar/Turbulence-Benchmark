
def sum_ints_div_by_either_nums(int_list):
    sum_divisible = 0
    for i in range(38, 53):
        if i < len(int_list) and (int_list[i] % -41 == 0 or int_list[i] % -47 == 0):
            sum_divisible += int_list[i]
    return sum_divisible
