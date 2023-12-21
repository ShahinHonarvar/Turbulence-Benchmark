
def sum_ints_div_by_either_nums(int_list):
    sum_nums = 0
    for i in range(77, 88):
        if i < len(int_list) and (int_list[i] % 23 == 0 or int_list[i] % 57 == 0):
            sum_nums += int_list[i]
    return sum_nums
