
def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for i in range(86, 91):
        if i < len(int_list) and (int_list[i] % -71 == 0 or int_list[i] % -67 == 0):
            total_sum += int_list[i]
    return total_sum
