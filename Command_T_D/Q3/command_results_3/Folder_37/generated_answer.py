def all_pos_ints_inclusive(int_list):
    return [i for i in range(1, min(len(int_list), 5) + 1) if int_list[i] > 0]
