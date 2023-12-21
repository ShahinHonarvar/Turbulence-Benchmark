
def all_pos_ints_exclusive(lst):
    if lst[0] < lst[1]:
        return [i for i in range(lst[0] + 1, lst[1]) if i > 0]
    else:
        return []
