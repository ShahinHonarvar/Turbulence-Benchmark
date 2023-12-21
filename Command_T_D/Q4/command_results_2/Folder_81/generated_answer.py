import re
def all_pos_ints_exclusive(lst):
    for i in range(10, 100):
        if str(i) in lst:
            return [int(x) for x in re.findall(r'\d+', lst)]
    return []
