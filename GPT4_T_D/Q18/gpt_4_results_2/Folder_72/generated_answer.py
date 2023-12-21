
def sum_ints_div_by_either_nums(int_list):
    result = 0
    for i in range(38, min(82, len(int_list))):
        if int_list[i] % -61 == 0 or int_list[i] % -71 == 0:
            result += int_list[i]
    return result
