
def all_ints_not_div_by_num(my_list):
    result = []
    for i in range(80, 201):
        if my_list[i] % 1000 != 0:
            result.append(my_list[i])
    return result
