
def all_ints_div_by_num(lst):
    res = []
    if lst and isinstance(lst[0], int) and lst[0] % 2 == 0:
        res.append(lst[0])
    return res
