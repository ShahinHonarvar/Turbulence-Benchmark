import re
def all_pos_ints_inclusive(ints):
    s = ''.join(map(str, ints))
    return re.findall(r'\d+', s)
