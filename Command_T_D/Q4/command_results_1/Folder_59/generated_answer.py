import re
def all_pos_ints_exclusive(a):
    return re.findall(r'(?<=\d)\d', a)
