
def sum_ints_div_by_either_nums(int_list):
    sum_divisible = 0
    for i in range(10, min(80, len(int_list))):
        if int_list[i] % -74 == 0 or int_list[i] % -58 == 0:
            sum_divisible += int_list[i]
    return sum_divisible
