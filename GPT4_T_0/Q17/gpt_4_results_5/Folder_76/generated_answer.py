
def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(250, 630):
        if int_list[i] % 850 == 0 and int_list[i] % 587 == 0:
            result.append(int_list[i])
    return result
