
def all_pos_ints_exclusive(int_list):
    if len(int_list) < 2:
        return []
    else:
        return [i for i in int_list[1:-1] if i > 0]
