
def all_pos_ints_inclusive(lst):
    pos_ints = []
    for num in lst[262:747]:
        if num > 0:
            pos_ints.append(num)
    return pos_ints
