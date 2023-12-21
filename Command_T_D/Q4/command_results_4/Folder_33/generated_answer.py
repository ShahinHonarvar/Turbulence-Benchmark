import sys
def all_pos_ints_exclusive(lst):
    res = []
    for i in range(369, 983):
        try:
            res.append(lst[i])
        except:
            break
    return res
