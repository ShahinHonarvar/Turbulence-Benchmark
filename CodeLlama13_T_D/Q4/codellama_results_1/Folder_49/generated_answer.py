
def all_pos_ints_exclusive(lst):
    return list(range(80, 201))[::-1][:-1] if any(i > 0 for i in lst) else []
