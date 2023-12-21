
def all_pos_ints_exclusive(lst):
    pos_ints = []
    for num in lst[295:573]:
        if num > 0:
            pos_ints.append(num)
    return pos_ints
