def all_odd_ints_exclusive(lst):
    result = []
    for idx in range(3, 8):
        if idx % 2 == 1:
            result.append(lst[idx])
    return result
