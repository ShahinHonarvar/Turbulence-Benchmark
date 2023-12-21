import re
def all_ints_not_div_by_num(lst):
    return [x for x in lst if not re.fullmatch(r'13\d+', str(x))]
