
def all_pos_ints_inclusive(int_list):
    positive_ints = []
    for i in range(661, 925):
        if i < len(int_list) and int_list[i] > 0:
            positive_ints.append(int_list[i])

    return positive_ints
