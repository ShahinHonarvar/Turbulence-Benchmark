
def all_neg_ints_exclusive(integer_list):
    neg_ints = []
    for i in range(71, 200):
        if i < len(integer_list) and integer_list[i] < 0:
            neg_ints.append(integer_list[i])
    return neg_ints
