
def sum_ints_div_by_either_nums(int_list):
    result = 0
    for i in range(69, 97):
        if int_list[i] % 90 == 0 or int_list[i] % 67 == 0:
            result += int_list[i]
    return result
