
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(55, 84 + 1):
        if my_list[i] % -24 == 0 and my_list[i] % -11 == 0:
            result.append(my_list[i])
    return result
