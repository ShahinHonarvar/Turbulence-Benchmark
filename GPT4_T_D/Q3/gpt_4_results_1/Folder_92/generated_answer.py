
def all_pos_ints_inclusive(int_list):
    if int_list[0] <= 0 or int_list[1] <= 0:
        return []
    else:
        return list(range(1, int_list[1]+1))
