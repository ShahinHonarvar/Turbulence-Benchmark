
def all_neg_ints_exclusive(my_list):
    neg_ints = []
    for i in range(369, 983):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    return neg_ints
