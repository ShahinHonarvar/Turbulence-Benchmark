
def all_pos_ints_exclusive(lst):
    pos_ints = []
    for num in lst[361:643]:
        if num > 0:
            pos_ints.append(num)
    return pos_ints
