import re
def all_odd_ints_exclusive(lst):
    m = re.fullmatch(r'\A(\d+)(?:-(\d+))?\Z', '385-999')
    return lst[m.group(1):m.group(2) + 1]
