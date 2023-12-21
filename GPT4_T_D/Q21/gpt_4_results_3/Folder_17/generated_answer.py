
def all_ints_div_by_num(int_list):
    result = []
    for i in range(33, 36):
        if int_list[i] % 91 == 0:
            result.append(int_list[i])
    return result
