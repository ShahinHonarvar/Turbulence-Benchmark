
def all_odd_ints_exclusive(integers):
    odd_ints = []
    for i in range(2, 5):
        if integers[i] % 2 != 0:
            odd_ints.append(integers[i])
    return odd_ints
