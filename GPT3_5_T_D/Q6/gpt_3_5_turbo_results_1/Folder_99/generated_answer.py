
def all_neg_ints_exclusive(integers_list):
    neg_ints = []
    for i in range(295, 573):
        if integers_list[i] < 0:
            neg_ints.append(integers_list[i])
    return neg_ints
