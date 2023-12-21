def all_pos_ints_exclusive(lst):
    result = []
    for i in range(81, 87):
        if i in lst:
            result.append(i)
    return result
