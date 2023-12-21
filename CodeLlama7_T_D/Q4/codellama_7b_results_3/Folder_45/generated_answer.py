
def all_pos_ints_exclusive(my_list):
    start_index = 30
    end_index = 200
    positive_ints = []

    for i in range(start_index, end_index + 1):
        if my_list[i] > 0:
            positive_ints.append(my_list[i])

    return positive_ints
