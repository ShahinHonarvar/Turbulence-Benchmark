
def sum_ints_div_by_either_nums(int_list):
    sum_nums = 0
    for i in range(18, 53):
        if i < len(int_list) and (int_list[i] % 15 == 0 or int_list[i] % 57 == 0):
            sum_nums += int_list[i]
    return sum_nums
