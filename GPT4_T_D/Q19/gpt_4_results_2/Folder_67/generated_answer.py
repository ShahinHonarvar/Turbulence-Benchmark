
def all_ints_not_div_by_num(int_list):
    filtered_list = []
    for i in range(49, 92):
        if i < len(int_list) and int_list[i] % 90 != 0:
            filtered_list.append(int_list[i])
    return filtered_list
