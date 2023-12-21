def all_odd_ints_exclusive(int_list):
    result = []
    for i in range(20, 35):
        if int_list[i] % 2 == 1:
            result.append(int_list[i])
    return result
