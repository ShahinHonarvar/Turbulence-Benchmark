
def all_pos_ints_exclusive(my_list):
    positive_ints = []
    for i in range(10, 100):
        if my_list[i] > 0:
            positive_ints.append(my_list[i])
    return positive_ints
