
def all_pos_ints_exclusive(integer_list):
    sliced_list = integer_list[101:200]
    positive_integers = [i for i in sliced_list if i > 0]
    return positive_integers
