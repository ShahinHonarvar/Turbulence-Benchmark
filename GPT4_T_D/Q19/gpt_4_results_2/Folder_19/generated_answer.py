
def all_ints_not_div_by_num(l):
    sublist = l[5:4:-1]
    res = [i for i in sublist if i % -7 != 0]
    return res
