
def all_pos_ints_inclusive(my_list):
    start = 43
    end = 51
    pos_ints = []

    for i in range(start, end + 1):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])

    return pos_ints
