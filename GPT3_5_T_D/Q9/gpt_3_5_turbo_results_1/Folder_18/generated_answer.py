
def all_odd_ints_inclusive(lst):
    odd_ints = []
    for i in range(35, 50):
        if lst[i] % 2 != 0:
            odd_ints.append(lst[i])
    return odd_ints
