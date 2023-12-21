
def all_pos_ints_exclusive(list_of_ints):
    return [int for int in range(4) if int in list_of_ints and int > 0]
