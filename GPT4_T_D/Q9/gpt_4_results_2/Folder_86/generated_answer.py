
def all_odd_ints_inclusive(lst):
    odd_ints = []
    for i in lst[31:35]:
        if i % 2 != 0:
            odd_ints.append(i)

    return odd_ints
