
def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(496, 826):
        if i < len(int_list):
            if int_list[i] % -201 != 0:
                result.append(int_list[i])
    return result
