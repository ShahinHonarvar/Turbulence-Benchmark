
def sum_ints_div_by_either_nums(int_list):
    sum_nums = 0
    for i in range(14, min(94, len(int_list))):
        if int_list[i] % 71 == 0 or int_list[i] % 81 == 0:
            sum_nums += int_list[i]
    return sum_nums
