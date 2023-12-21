
def all_pos_ints_inclusive(input_list):
    pos_ints = []
    for i in range(62, 100):
        if i < len(input_list) and input_list[i] > 0:
            pos_ints.append(input_list[i])
    return pos_ints
