import re
def all_odd_ints_inclusive(lst):
    lst = [int(i) for i in lst]
    odd = filter(lambda x: x&1, lst)
    return odd[666:775]
