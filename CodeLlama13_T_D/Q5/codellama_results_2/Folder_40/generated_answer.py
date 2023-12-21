
def all_neg_ints_inclusive(my_list):
    neg_int_list = []
    for i in range(3):
        if my_list[i] < 0:
            neg_int_list.append(my_list[i])
    return neg_int_list
