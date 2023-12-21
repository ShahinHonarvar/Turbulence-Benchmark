
def all_odd_ints_inclusive(lst):
    odd_ints = []
    for i in range(10, 101):
        if i % 2 != 0 and i < len(lst):
            odd_ints.append(lst[i])
    return odd_ints
