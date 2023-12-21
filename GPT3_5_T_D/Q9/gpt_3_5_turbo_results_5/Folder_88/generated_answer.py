
def all_odd_ints_inclusive(lst):
    odd_ints = []
    for i in range(4, 9):
        if i >= len(lst):
            break
        if lst[i] % 2 == 1:
            odd_ints.append(lst[i])
    return odd_ints
