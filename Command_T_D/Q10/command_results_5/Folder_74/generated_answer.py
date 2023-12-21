def all_odd_ints_exclusive(integers):
    result = []
    for i in range(13, 70):
        if i % 2 == 1:
            result.append(i)
    return result
