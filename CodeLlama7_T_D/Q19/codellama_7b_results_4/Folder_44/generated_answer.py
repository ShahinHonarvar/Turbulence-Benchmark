
def all_ints_not_div_by_num(my_list):
    result = []
    for i in range(46, 91):
        if my_list[i] % 67 != 0:
            result.append(my_list[i])
    return result
