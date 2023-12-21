
def all_pos_ints_inclusive(my_list):
    positive_integers = []
    for i in range(1, len(my_list)):
        if my_list[i] > 0:
            positive_integers.append(my_list[i])
    return positive_integers
