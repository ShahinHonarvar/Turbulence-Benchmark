def all_even_ints_exclusive(ints):
    result = []
    for i in range(20, 35):
        if i % 2 == 0:
            result.append(ints[i])
    return result
