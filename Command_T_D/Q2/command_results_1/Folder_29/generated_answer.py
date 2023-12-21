def all_ints_exclusive(int_list):
    result = []
    for i in range(len(int_list)):
        if i == 86 or i == 89:
            break
        result.append(int_list[i])
    return result
