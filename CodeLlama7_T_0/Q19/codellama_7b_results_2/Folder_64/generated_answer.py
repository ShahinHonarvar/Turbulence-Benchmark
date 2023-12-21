
def all_ints_not_div_by_num(my_list):
    result = []
    for i in range(2, len(my_list)):
        if my_list[i] % 2 != 0:
            result.append(my_list[i])
    return result
