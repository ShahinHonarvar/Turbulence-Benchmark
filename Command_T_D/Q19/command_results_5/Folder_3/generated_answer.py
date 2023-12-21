import re
def all_ints_not_div_by_num(a):
    return [x for x in a[30:70] if not x%(-70)]
