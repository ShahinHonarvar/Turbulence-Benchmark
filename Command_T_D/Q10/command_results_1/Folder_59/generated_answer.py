def all_odd_ints_exclusive(lst):
    result = []
    for i in range(0, len(lst) - 1):
        if lst[i] % 2 == 1:
            result.append(lst[i])
    if lst[-1] % 2 == 1:
        result.append(lst[-1])
    return result
