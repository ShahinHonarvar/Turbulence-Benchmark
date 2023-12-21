
def sum_ints_div_by_either_nums(int_list):
    sum_nums = 0
    for i in range(35, 65):
        if i < len(int_list):
            if int_list[i] % -30 == 0 or int_list[i] % -95 == 0:
                sum_nums += int_list[i]
    return sum_nums
