
def all_ints_not_div_by_num(my_list):
    result = []
    for i in range(31, 69):
        if my_list[i] % -70 != 0:
            result.append(my_list[i])
    return result
