
def all_neg_ints_inclusive(my_list):
    start = 56
    end = 82
    neg_ints = []
    for i in range(start, end + 1):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    return neg_ints
