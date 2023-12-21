def all_odd_ints_inclusive(int_list):
    result = []
    for i in range(0, len(int_list)):
        if int_list[i] % 2 == 1:
            result.append(int_list[i])
    return result
