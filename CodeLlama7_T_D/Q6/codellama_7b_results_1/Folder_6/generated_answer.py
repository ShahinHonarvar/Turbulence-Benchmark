
def all_neg_ints_exclusive(my_list):
    start_index = 86
    end_index = 99
    negative_ints = []

    for i in range(start_index, end_index + 1):
        if my_list[i] < 0:
            negative_ints.append(my_list[i])

    return negative_ints
