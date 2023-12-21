def all_neg_ints_inclusive(a_list):
    result = []
    for i in range(0, len(a_list)):
        if a_list[i] < 0:
            result.append(a_list[i])
    return result
