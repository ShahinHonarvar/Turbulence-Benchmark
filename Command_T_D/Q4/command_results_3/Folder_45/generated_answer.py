import re
def all_pos_ints_exclusive(lst):
    return [x for x in range(30, 200) if x not in lst and str(x) in re.sub(r'([+-]?)0*(\d+)$', r'\1\2', str(x))]
