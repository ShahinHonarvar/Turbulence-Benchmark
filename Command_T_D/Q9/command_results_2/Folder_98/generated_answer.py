def all_odd_ints_inclusive(lst):
    result = []
    for i in range(0, len(lst)):
        if lst[i] % 2 == 1:
            result.append(lst[i])
    return result
