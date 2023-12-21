import sys
def all_ints_div_by_num(a):
    return [i for i in range(len(a)) if a[i] % 8 == 0]
