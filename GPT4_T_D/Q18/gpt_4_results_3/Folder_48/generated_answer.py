
def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for index in range(306, 958):
        if index < len(int_list) and (int_list[index] % 982 == 0 or int_list[index] % 319 == 0):
            total_sum += int_list[index]
    return total_sum
