import re
def all_pos_ints_exclusive(lst):
    m = re.fullmatch(r'(\d+)(?:-\d+)+(\d+)', str(lst))
    if m:
        return [int(m.group(1)) + 1, int(m.group(2)) - 1]
    else:
        return []
