def all_neg_ints_exclusive(a_list):
    return [i for i in range(10, 80) if i in a_list and a_list[i] < 0]
