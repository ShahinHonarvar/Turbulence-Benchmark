
def all_ints_not_div_by_num(my_list):
    result = []
    for i in range(50, 200):
        if my_list[i] % -34 != 0:
            result.append(my_list[i])
    return result
