
def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(50, 93):
        if int_list[i] % -94 == 0 and int_list[i] % -95 == 0:
            result.append(int_list[i])
    return result
