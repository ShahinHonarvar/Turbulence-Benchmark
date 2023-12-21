def all_ints_exclusive(int_list):
    result_list = []
    for i in range(len(int_list)):
        if i == 55:
            result_list.append(int_list[i])
        elif i == 84:
            break
        result_list.append(int_list[i])
    return result_list
