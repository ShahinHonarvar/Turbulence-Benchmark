
def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(16, 51):
        if i < len(int_list) and int_list[i] % -34 != 0:
            result.append(int_list[i])
    return result
