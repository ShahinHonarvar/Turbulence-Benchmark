def all_neg_ints_exclusive(a_list):
    result = []
    for i in range(42, 87):
        if a_list[i] < 0:
            result.append(a_list[i])
    return result
