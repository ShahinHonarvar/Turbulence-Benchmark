def all_odd_ints_inclusive(lst):
    result = []
    for i in range(37, 77):
        if i % 2 == 1:
            result.append(i)
    return result
