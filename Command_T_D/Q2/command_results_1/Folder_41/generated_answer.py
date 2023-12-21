def all_ints_exclusive(int_list):
    result = []
    for i in range(3, len(int_list) - 1):
        result.append(int_list[i])
    for j in range(len(int_list) - 2, -1, -1):
        result.append(int_list[j])
    return result
