def all_odd_ints_inclusive(int_list):
    result = []
    for i in range(22, 88, 2):
        if int_list[i] % 2 == 0:
            result.append(int_list[i])
    return result
