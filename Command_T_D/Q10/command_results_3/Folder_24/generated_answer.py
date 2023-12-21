def all_odd_ints_exclusive(lst):
    result = []
    if lst[12] % 2 != 0:
        result.append(lst[12])
    if lst[65] % 2 != 0:
        result.append(lst[65])
    for i in range(13, 65):
        if lst[i] % 2 != 0:
            result.append(lst[i])
    return result
