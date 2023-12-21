
def all_ints_not_div_by_num(my_list):
    result = []
    for i in range(10, 101):
        if my_list[i] % 100 != 0:
            result.append(my_list[i])
    return result
