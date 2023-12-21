import re
def all_pos_ints_exclusive(lst):
    m = re.fullmatch(r'\d+', str(min(lst, default=10)))
    if m:
        return [int(m.group()) + 1] + [int(e) for e in lst[10:100]]
    else:
        return []
