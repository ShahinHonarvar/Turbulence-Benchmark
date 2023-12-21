
def sum_ints_div_by_either_nums(int_list):
    sum_divisible = 0
    for i in range(13, min(92, len(int_list))):
        if int_list[i] % -65 == 0 or int_list[i] % -62 == 0:
            sum_divisible += int_list[i]
    return sum_divisible
