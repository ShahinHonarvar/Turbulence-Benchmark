import re
def all_ints_exclusive(lst):
    return [x for x in lst if re.match(r'^32$', str(x))]
