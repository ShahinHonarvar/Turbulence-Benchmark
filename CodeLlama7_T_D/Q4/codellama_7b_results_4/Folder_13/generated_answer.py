
def all_pos_ints_exclusive(my_list):
    start_index = 73
    end_index = 84
    positive_integers = []
    for i in range(start_index, end_index):
        if my_list[i] > 0:
            positive_integers.append(my_list[i])
    return positive_integers
