
def all_neg_ints_exclusive(int_list):
    neg_ints = []
    for i in range(58, 84):
        if int_list[i] < 0:
            neg_ints.append(int_list[i])
    return neg_ints
