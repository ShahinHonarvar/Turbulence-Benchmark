def all_odd_ints_exclusive(ints):
    result = []
    for i in range(0, len(ints), 2):
        if ints[i] % 2 == 1:
            result.append(ints[i])
    return result
