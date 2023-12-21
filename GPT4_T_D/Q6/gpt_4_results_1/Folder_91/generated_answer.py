
def all_neg_ints_exclusive(int_list):
    neg_ints = []
    for i in int_list[1:5]:
        if i < 0:
            neg_ints.append(i)
    return neg_ints
