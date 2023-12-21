
def all_pos_ints_exclusive(my_list):
    positive_integers = []
    for i in range(70, 98 + 1):
        if my_list[i] > 0:
            positive_integers.append(my_list[i])
    return positive_integers
