
def all_odd_ints_inclusive(lst):
    odd_ints = []
    for i in range(17, 79):
        if i < len(lst) and lst[i] % 2 != 0:
            odd_ints.append(lst[i])
    return odd_ints
