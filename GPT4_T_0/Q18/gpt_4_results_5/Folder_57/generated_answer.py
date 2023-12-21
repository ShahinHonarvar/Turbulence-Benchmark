
def sum_ints_div_by_either_nums(int_list):
    sum_divisible = 0
    for i in range(51, 77):
        if i < len(int_list) and (int_list[i] % -90 == 0 or int_list[i] % -59 == 0):
            sum_divisible += int_list[i]
    return sum_divisible
