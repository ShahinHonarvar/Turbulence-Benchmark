
def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(669, 739):
        if i < len(int_list) and int_list[i] % -172 != 0:
            result.append(int_list[i])
    return result
