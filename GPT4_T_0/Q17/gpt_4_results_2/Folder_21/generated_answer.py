
def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(315, 935):
        if int_list[i] % -897 == 0 and int_list[i] % -556 == 0:
            result.append(int_list[i])
    return result
