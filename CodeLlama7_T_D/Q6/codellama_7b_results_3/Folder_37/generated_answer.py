
def all_neg_ints_exclusive(my_list):
    neg_ints = []
    for i in range(1, len(my_list)):
        if my_list[i - 1] < 0 and my_list[i] > 0:
            neg_ints.append(my_list[i - 1])
    return neg_ints
