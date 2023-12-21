
def all_neg_ints_exclusive(my_list):
    start = 15
    end = 40
    neg_ints = []
    for i in range(start, end):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    return neg_ints
