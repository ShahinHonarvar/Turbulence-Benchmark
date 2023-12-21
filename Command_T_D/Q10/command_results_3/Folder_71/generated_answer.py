def all_odd_ints_exclusive(lst):
    result = []
    for idx in range(len(lst) - 1, -1, -2):
        if lst[idx] % 2:
            result.append(lst[idx])
    return result
