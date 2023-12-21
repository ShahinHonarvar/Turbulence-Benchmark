
def all_pos_ints_inclusive(lst):
    if lst[0] > 0 and lst[1] > 0:
        return [i for i in range(lst[0], lst[1] + 1) if i > 0]
    else:
        return []
