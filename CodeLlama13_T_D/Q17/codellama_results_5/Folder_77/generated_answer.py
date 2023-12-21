
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(828, 933):
        if my_list[i] % -649 == 0 and my_list[i] % -461 == 0:
            result.append(my_list[i])
    return result
