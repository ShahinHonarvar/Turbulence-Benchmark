def all_odd_ints_exclusive(int_list):
    result = []
    for index in range(20, 35):
        if index % 2 == 1:
            result.append(int_list[index])
    return result
