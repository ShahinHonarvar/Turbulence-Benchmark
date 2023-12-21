
def all_pos_ints_exclusive(integer_list):
    positive_integers = []
    for i in range(277, 376):
        if integer_list[i] > 0:
            positive_integers.append(integer_list[i])
    return positive_integers
