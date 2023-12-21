
def all_pos_ints_exclusive(int_list):
    if len(int_list) < 4:
        return []
    else:
        positive_ints = [i for i in int_list[1:3] if i > 0]
        return positive_ints
