def all_ints_exclusive(lst):
    result = []
    for i in range(len(lst) - 1):
        result.append(lst[i])
    result.append(lst[0])
    return result
