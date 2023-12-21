
def all_pos_ints_exclusive(lst):
    res = []
    for index in range(56, 84):
        if lst[index] > 0:
            res.append(lst[index])
    return res
