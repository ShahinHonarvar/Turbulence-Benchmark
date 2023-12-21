def all_odd_ints_inclusive(ints):
    result = []
    for i in range(10, 100):
        if i % 2 == 1:
            result.append(ints[i])
    return result
