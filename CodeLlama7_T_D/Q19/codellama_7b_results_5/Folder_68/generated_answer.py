
def all_ints_not_div_by_num(my_list):
    result = []
    for i in range(len(my_list)):
        if my_list[i] % 7 != 0:
            result.append(my_list[i])
    return result
