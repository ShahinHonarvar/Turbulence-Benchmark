
def all_ints_not_div_by_num(my_list):
    result = []
    for i in range(4, 5):
        if my_list[i] % -7 != 0:
            result.append(my_list[i])
    return result
