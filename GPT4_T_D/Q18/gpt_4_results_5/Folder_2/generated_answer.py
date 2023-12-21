
def sum_ints_div_by_either_nums(num_list):
    summation = 0
    for i in range(73, 87):
        if i<len(num_list) and (num_list[i] % 54 == 0 or num_list[i] % 82 == 0):
            summation += num_list[i]
    return summation
