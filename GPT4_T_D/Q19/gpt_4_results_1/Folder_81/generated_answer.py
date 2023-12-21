
def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(11, min(100, len(int_list))):
        if int_list[i] % 100 != 0:
            result.append(int_list[i])
    return result
