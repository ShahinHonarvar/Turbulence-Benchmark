def all_odd_ints_inclusive(lst):
    result = []
    for i in range(4, 8):
        if lst[i] % 2:
            result.append(lst[i])
    return result
