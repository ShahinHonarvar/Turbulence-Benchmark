
def all_pos_ints_inclusive(lst):
    if lst[0] <= 0 or lst[1] <= 0:
        return []
    else:
        return list(range(lst[0], lst[1] + 1))
