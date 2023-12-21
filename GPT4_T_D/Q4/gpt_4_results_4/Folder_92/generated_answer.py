
def all_pos_ints_exclusive(lst):
    if len(lst) < 2:
        return []
    sub_list = lst[1:-1]
    pos_ints = [i for i in sub_list if i > 0]
    return pos_ints
