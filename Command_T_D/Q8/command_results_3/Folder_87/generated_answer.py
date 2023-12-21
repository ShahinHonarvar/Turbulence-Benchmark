def all_even_ints_exclusive(lst):
    result = []
    for i in range(32, 99):
        if i % 2 == 0:
            result.append(i)
    return result
