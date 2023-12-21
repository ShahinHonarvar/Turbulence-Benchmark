def all_pos_ints_exclusive(a_list):
    res = []
    i = 0
    while i < len(a_list) and a_list[i] > 0:
        res.append(a_list[i])
        i += 1
    return res
