
def all_neg_ints_exclusive(my_list):
    start_index = 48
    end_index = 76
    negative_ints = []
    for i in range(start_index, end_index):
        if my_list[i] < 0:
            negative_ints.append(my_list[i])
    return negative_ints
