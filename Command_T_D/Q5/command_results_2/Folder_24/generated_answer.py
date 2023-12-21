def all_neg_ints_inclusive(lst):
    result = []
    i = lst[74]
    while i != lst[95]:
        if i < 0:
            result.append(i)
        i += 1
    return result
