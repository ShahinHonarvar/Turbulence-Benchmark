
def all_neg_ints_inclusive(my_list):
    start_index = 4
    end_index = 4
    neg_ints = []
    for i in range(start_index, end_index + 1):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    return neg_ints
