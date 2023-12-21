
def sum_ints_div_by_either_nums(int_list):
    result_sum = 0
    for i in range(38, 82):
        if i < len(int_list) and (int_list[i] % -61 == 0 or int_list[i] % -71 == 0):
            result_sum += int_list[i]
    return result_sum
