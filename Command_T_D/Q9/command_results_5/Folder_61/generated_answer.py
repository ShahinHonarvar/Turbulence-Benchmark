def all_odd_ints_inclusive(list):
    result = []
    for i in range(0, 8):
        if i % 2 == 1:
            result.append(list[i])
    return result
