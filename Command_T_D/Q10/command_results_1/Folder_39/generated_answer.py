def all_odd_ints_exclusive(int_list):
    result = []
    for idx in range(43, 99):
        if idx % 2 == 1:
            result.append(int_list[idx])
    return result
