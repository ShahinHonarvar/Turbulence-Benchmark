
def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(21, 35):
        if int_list[i] % -36 != 0:
            result.append(int_list[i])
    return result
