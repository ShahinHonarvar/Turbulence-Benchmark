def all_pos_ints_exclusive(a_list):
    result = []
    for i in range(44, 78):
        if i < 0:
            continue
        elif i not in a_list:
            continue
        elif a_list[i] >= 0:
            result.append(a_list[i])
    return result
