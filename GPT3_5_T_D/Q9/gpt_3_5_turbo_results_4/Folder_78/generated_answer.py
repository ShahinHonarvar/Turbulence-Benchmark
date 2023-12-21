
def all_odd_ints_inclusive(lst):
    odd_ints = []
    for i in range(43, 52):
        if lst[i] % 2 == 1:
            odd_ints.append(lst[i])
    return odd_ints
