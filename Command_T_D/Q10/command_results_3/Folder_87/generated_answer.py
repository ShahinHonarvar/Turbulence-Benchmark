import re
def all_odd_ints_exclusive(lst):
    s = ' '.join(str(x) for x in lst)
    return re.findall(r'(?<=\d{2})\d{2}(?=\d{2})', s)
