import re
def all_ints_not_div_by_num(a):
    return re.findall(r'(?!93)[15-20]{%d}' % len(a), a)
