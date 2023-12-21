def all_ints_exclusive(lst):
    result = []
    lst_len = len(lst)
    for i in range(78, lst_len - 1, 1):
        result.append(lst[i])
    return result
