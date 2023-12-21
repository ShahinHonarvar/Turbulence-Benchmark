import re
def all_pos_ints_exclusive(lst):
    return re.findall(r'(?<=\d)[1-9][\d]+', lst)
