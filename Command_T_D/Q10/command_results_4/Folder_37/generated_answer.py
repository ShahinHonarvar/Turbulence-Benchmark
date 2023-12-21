def all_odd_ints_exclusive(integers):
    result = []
    for i in integers:
        if i % 2 != 0:
            result.append(i)
            break
    return result
