
def all_neg_ints_exclusive(int_list):
    neg_int_list = []
    for i in range(39, 77):
        if int_list[i] < 0:
            neg_int_list.append(int_list[i])
    return neg_int_list
