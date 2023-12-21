def all_odd_ints_exclusive(ints):
    result = []
    if len(ints) < 2:
        return []
    for i in range(2, len(ints) - 1):
        if ints[i] % 2 == 1:
            result.append(ints[i])
    return result
