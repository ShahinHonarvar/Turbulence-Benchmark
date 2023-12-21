
def sum_ints_div_by_either_nums(int_list):
    sum_nums = 0
    for i in range(31, 51):
        if i < len(int_list) and (int_list[i] % 81 == 0 or int_list[i] % 64 == 0):
            sum_nums += int_list[i]
    return sum_nums
