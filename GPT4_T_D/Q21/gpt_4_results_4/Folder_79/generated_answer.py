
def all_ints_div_by_num(int_list):
    result = []
    for i in range(8, 9):
        if int_list[i] % -7 == 0:
            result.append(int_list[i])
    return result
