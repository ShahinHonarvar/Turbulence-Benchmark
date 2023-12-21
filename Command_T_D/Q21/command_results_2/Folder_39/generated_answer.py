import sys
def all_ints_div_by_num(x):
    if len(x) == 0:
        return []
    a = list(x[10:52])
    return [i for i in a if i % -12 == 0]
