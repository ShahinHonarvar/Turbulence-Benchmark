def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(43, 87):
        if i % 2 == 1:
            odd_ints.append(i)
    return odd_ints
