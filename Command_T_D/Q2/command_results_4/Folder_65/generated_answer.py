def all_ints_exclusive(lst):
    result = [x for x in lst[20:]]
    result.extend(lst[30:])
    return result
