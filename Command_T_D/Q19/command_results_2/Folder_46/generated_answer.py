import re
def all_ints_not_div_by_num(lst):
    s = str(lst)
    return [int(x) for x in re.findall(r'([0-9]+)', s[18:-2]) if not x % 86]
