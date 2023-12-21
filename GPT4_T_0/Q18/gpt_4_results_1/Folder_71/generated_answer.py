
def sum_ints_div_by_either_nums(int_list):
    sum_divisible = 0
    for i in range(68, min(100, len(int_list))):
        if int_list[i] % -37 == 0 or int_list[i] % -26 == 0:
            sum_divisible += int_list[i]
    return sum_divisible
