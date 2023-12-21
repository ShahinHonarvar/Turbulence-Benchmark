
def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(209, 557):
        if i % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints
