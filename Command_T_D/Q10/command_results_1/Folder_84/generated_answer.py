def all_odd_ints_exclusive(lst):
    result = []
    for i in range(50, 92):
        if i % 2 == 1:
            result.append(i)
    return result
