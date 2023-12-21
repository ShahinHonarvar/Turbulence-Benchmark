
def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(2):
        if int_list[i] % -6 == 0 and int_list[i] % 4 == 0:
            result.append(int_list[i])
    return result
