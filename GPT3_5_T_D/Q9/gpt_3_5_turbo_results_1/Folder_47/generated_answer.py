
def all_odd_ints_inclusive(lst):
    odd_ints = []
    for i in range(37, 77):
        if i >= len(lst):
            break
        if lst[i] % 2 != 0:
            odd_ints.append(lst[i])
    return odd_ints
