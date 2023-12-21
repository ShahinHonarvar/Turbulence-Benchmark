def all_odd_ints_exclusive(list):
    result = []
    for i in range(0, 10, 2):
        if list[i] % 2 == 1:
            result.append(list[i])
    return result
