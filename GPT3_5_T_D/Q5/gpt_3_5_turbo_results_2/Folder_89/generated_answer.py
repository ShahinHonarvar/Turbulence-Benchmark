
def all_neg_ints_inclusive(integers):
    negative_ints = []
    for i in range(56, 83):
        if integers[i] < 0:
            negative_ints.append(integers[i])
    return negative_ints
