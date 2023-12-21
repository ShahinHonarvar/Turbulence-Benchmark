
def all_pos_ints_inclusive(my_list):
    start_index = 70
    end_index = 84
    pos_ints = []
    for i in range(start_index, end_index + 1):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
