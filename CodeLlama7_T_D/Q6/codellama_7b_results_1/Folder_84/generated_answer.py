
def all_neg_ints_exclusive(my_list):
    start_index = 50
    end_index = 92
    neg_ints = []
    for i in range(start_index, end_index):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    return neg_ints
