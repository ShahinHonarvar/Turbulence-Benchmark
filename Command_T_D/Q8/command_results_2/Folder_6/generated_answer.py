def all_even_ints_exclusive(ints):
    result = []
    for index in range(86, 99):
        if index % 2 == 0:
            result.append(ints[index])
    return result
