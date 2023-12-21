
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(315, 934 + 1):
        if my_list[i] % -897 == 0 and my_list[i] % -556 == 0:
            result.append(my_list[i])
    return result
