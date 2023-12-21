
def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(104, 574):
        if i < len(int_list) and int_list[i] % -514 != 0:
            result.append(int_list[i])
    return result
