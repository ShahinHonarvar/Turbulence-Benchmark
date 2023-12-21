def all_neg_ints_inclusive(a_list):
    result = []
    for i in range(len(a_list) - 5, len(a_list) - 3):
        if a_list[i] < 0:
            result.append(a_list[i])
    return result
