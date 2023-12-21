def all_neg_ints_inclusive(list):
    negative_ints = []
    for i in range(55,98):
        if list[i] < 0:
            negative_ints.append(list[i])
    return negative_ints
