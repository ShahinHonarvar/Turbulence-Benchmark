
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(306, 958):
        if my_list[i] % 982 == 0 and my_list[i] % 319 == 0:
            result.append(my_list[i])
    return result
