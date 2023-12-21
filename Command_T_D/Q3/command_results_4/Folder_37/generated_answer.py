def all_pos_ints_inclusive(lst):
    return [x for x in range(1, len(lst)+1) if x > 0 and x <= 5 and lst[x-1] == x]
