
def sum_ints_div_by_either_nums(int_list):
    sum_divisible_nums = 0
    for i in range(3):
        if i<len(int_list) and (int_list[i] % -2 == 0 or int_list[i] % 3 == 0):
            sum_divisible_nums += int_list[i]
    return sum_divisible_nums
