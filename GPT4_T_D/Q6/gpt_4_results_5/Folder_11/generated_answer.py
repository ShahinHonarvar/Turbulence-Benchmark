
def all_neg_ints_exclusive(int_list):
    neg_ints = []
    for i in range(16, 99):
        if i < len(int_list) and int_list[i] < 0:
            neg_ints.append(int_list[i])
    return neg_ints
