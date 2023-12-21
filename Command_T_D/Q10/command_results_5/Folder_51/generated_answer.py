def all_odd_ints_exclusive(lst):
    result = []
    for i in range(6, 9):
        if lst[i] % 2:
            result.append(lst[i])
    return result
