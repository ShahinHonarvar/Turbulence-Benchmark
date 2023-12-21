
def all_ints_not_div_by_num(my_list):
    result = []
    for i in range(469, 566):
        if my_list[i] % -692 != 0:
            result.append(my_list[i])
    return result
