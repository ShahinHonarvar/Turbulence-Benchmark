
def all_odd_ints_exclusive(lst):
    odd_ints = []
    for i in range(20, 36):
        if lst[i] % 2 != 0:
            odd_ints.append(lst[i])
    return odd_ints
