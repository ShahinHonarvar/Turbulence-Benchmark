def all_pos_ints_exclusive(lst):
    result = []
    for i in range(13, 70):
        if i not in lst:
            result.append(i)
    return result
