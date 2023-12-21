
def all_ints_div_by_both_two_nums(int_list):
    result = []
    if int_list:
        if int_list[0] % 1 == 0 and int_list[0] % -1 == 0:
            result.append(int_list[0])
    return result
