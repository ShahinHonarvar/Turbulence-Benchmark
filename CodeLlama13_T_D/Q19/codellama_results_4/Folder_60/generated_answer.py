
def all_ints_not_div_by_num(my_list):
    result = []
    for i in range(63, 74):
        if my_list[i] % -99 != 0:
            result.append(my_list[i])
    return result
