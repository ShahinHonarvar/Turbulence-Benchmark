
def all_pos_ints_inclusive(lst):
    if lst[0] > lst[1] or lst[0] < 1 or lst[1] < 1:
        return []
    else:
        return [i for i in range(lst[0], lst[1]+1) if i > 0]
