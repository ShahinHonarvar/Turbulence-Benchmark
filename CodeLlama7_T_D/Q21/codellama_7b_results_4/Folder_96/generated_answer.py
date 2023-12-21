
def all_ints_div_by_num(my_list):
    result = []
    for i in range(20, len(my_list)):
        if my_list[i] % 2 == 0:
            result.append(my_list[i])
    return result
