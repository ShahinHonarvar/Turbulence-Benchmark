
def sum_ints_div_by_either_nums(int_list):
    sum_nums = 0
    for i in range(25, min(71, len(int_list))):
        if int_list[i] % 74 == 0 or int_list[i] % 15 == 0:
            sum_nums += int_list[i]
    return sum_nums
