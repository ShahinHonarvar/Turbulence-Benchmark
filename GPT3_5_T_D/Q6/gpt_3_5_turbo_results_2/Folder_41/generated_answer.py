
def all_neg_ints_exclusive(integers):
    negative_ints = []
    for i in range(8, 9):
        if integers[i] < 0:
            negative_ints.append(integers[i])
    return negative_ints
