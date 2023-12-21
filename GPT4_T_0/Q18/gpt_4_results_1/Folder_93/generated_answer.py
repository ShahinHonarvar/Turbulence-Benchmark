
def sum_ints_div_by_either_nums(int_list):
    sum_nums = 0
    for i in range(86, 90):
        if i < len(int_list) and (int_list[i] % -61 == 0 or int_list[i] % -79 == 0):
            sum_nums += int_list[i]
    return sum_nums
