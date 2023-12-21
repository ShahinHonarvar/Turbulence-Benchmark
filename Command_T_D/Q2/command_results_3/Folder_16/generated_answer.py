def all_ints_exclusive(ints):
    result = []
    for i in range(len(ints)-1, 39, -1):
        if i < 43:
            result.append(ints[i])
    return result
