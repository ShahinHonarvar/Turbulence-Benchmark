def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(35, 49):
        if int_list[i] % 2 == 1:
            odd_ints.append(int_list[i])
    return odd_ints
