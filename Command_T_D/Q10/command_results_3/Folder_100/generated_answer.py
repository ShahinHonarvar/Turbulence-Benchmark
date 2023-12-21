def all_odd_ints_exclusive(lst):
    result = []
    for i in range(22, 24):
        if lst[i] % 2 == 1:
            result.append(lst[i])
    return result
