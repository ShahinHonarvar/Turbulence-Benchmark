
def all_pos_ints_exclusive(my_list):
    return [i for i in range(1, len(my_list)) if my_list[i-1] > 0 and my_list[i] > 0]
