def all_ints_exclusive(lst):
    result = []
    for item in range(86, 99):
        if item not in lst:
            break
        result.append(item)
    return result
