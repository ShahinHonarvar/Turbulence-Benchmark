def all_pos_ints_exclusive(a_list):
    res = []
    for i in range(20, 200):
        if i not in a_list:
            res.append(i)
    return res
