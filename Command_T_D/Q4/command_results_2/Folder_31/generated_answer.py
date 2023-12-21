def all_pos_ints_exclusive(lst):
    result = []
    for i in range(87, 95):
        if i in lst and lst[i] > 0:
            result.append(lst[i])
    return result
