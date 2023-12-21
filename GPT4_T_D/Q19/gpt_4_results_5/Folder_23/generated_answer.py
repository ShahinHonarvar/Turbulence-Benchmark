
def all_ints_not_div_by_num(int_list):
    result_list = []
    for i in range(45, 91):
        if i < len(int_list) and int_list[i] % -68 != 0:
            result_list.append(int_list[i])
    return result_list
