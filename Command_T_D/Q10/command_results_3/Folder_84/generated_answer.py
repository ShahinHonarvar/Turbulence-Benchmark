def all_odd_ints_exclusive(lst):
    result = []
    lst = lst[50:-2]
    for item in lst:
        if item % 2 == 1:
            result.append(item)
    return result
