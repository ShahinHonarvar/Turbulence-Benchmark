
def sum_ints_div_by_either_nums(int_list):
    sum_divisible = 0
    for i in range(10, 29):
        if i < len(int_list) and (int_list[i] % -61 == 0 or int_list[i] % -64 == 0):
            sum_divisible += int_list[i]
    return sum_divisible
