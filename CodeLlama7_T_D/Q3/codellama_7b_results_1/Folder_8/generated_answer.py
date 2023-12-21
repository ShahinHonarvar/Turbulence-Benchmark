
def all_pos_ints_inclusive(my_list):
    start_index = 23
    end_index = 23
    pos_ints = []

    for i in range(start_index, end_index + 1):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])

    return pos_ints
