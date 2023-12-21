import re
def all_pos_ints_exclusive(lst):
    return [x for x in range(100, 200, 1) if re.match(".*\d+$", str(x)) and x > 0]
