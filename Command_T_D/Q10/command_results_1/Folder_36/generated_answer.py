import re
def all_odd_ints_exclusive(lst):
    return [i for i in range(598, 767, 2) if str(i) in re.findall(r'\d+', lst)]
