
def all_odd_ints_inclusive(lst):
    if isinstance(lst[0], int) and lst[0] % 2 != 0:
        return [lst[0]]
    else:
        return []
