def all_odd_ints_inclusive(int_list):
    if not int_list:
        return []
    start, stop = 50, 54
    odd_ints = []
    for i in range(start, stop):
        if int_list[i] % 2 == 0:
            odd_ints.append(int_list[i])
    return odd_ints
