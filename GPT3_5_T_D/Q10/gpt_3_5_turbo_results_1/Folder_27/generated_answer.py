
def all_odd_ints_exclusive(lst):
    odd_ints = []
    for i in lst[28:49]:
        if i % 2 != 0:
            odd_ints.append(i)
    return odd_ints
