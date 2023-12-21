
def all_neg_ints_inclusive(int_list):
    neg_ints_15_to_39 = []
    for i in range(15, 40):
        if i<len(int_list) and int_list[i] < 0:
            neg_ints_15_to_39.append(int_list[i])
    return neg_ints_15_to_39
