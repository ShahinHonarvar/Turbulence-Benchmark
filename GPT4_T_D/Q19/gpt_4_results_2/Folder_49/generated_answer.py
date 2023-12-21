
def all_ints_not_div_by_num(int_list):
    result_list = []
    for i in range(81, 200):
        if i < len(int_list):
            if int_list[i] % 1000 != 0:
                result_list.append(int_list[i])
    return result_list
