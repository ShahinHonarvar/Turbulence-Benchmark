
def sum_ints_div_by_either_nums(int_list):
    sum_nums = 0
    for i in range(44, 60):
        if i < len(int_list) and (int_list[i] % 39 == 0 or int_list[i] % 15 == 0):
            sum_nums += int_list[i]
    return sum_nums
