
def all_ints_div_by_num(my_list):
    result = []
    for i in range(161, 970 + 1):
        if my_list[i] % 763 == 0:
            result.append(my_list[i])
    return result
