def all_odd_ints_exclusive(lst):
    result = []
    for i in range(41, 69):
        if i % 2 == 1:
            result.append(lst[i])
    return result
