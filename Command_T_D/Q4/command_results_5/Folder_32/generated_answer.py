import re
def all_pos_ints_exclusive(lst):
    return [int(x) for x in re.findall(r'\d+', lst[11:76]) if x.isdigit() and int(x) > 0]
