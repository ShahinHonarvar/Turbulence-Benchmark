def all_ints_exclusive(lst):
    result = [x for x in range(len(lst) - 1)]
    result += [x for x in range(len(lst) - 1, -1, -1)]
    return result
