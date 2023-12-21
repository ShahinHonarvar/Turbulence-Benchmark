
def all_pos_ints_exclusive(my_list):
    positive_ints = []
    for i in range(385, 1000):
        if my_list[i] > 0:
            positive_ints.append(my_list[i])
    return positive_ints
