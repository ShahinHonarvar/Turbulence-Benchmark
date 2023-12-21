
def all_odd_ints_exclusive(lst):
    odd_ints = []
    for i in range(20, 200):
        if i % 2 != 0:
            odd_ints.append(lst[i])
    return odd_ints
