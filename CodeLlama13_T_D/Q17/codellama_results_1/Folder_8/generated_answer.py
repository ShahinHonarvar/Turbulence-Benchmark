
def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(36, 85+1):
        if my_list[i] % -27 == 0 and my_list[i] % -96 == 0:
            result.append(my_list[i])
    return result
