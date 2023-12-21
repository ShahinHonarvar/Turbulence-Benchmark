import re
def all_ints_not_div_by_num(lst):
    return [x for x in range(25, 77) if re.fullmatch(r'[25-76]+', str(x)) and not x % -53]
