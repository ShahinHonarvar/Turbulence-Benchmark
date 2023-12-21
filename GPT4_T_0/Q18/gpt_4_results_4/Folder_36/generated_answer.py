
def sum_ints_div_by_either_nums(int_list):
    sum_nums = 0
    for i in range(299, 383):
        if i < len(int_list) and (int_list[i] % 858 == 0 or int_list[i] % 952 == 0):
            sum_nums += int_list[i]
    return sum_nums
