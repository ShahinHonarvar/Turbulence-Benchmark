
def all_pos_ints_exclusive(my_list):
    start_index = 78
    end_index = 93
    pos_ints = []
    for i in range(start_index, end_index):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
