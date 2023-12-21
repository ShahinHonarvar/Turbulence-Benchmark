def all_ints_exclusive(lst):
    result = [x for x in range(0, 10)]
    result += [y for y in lst if y not in result]
    return result
