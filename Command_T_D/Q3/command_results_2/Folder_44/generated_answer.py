import re
def all_pos_ints_inclusive(lst):
    return [i for i in range(13,69) if str(i) in re.findall(r'[0-9]+', lst)]
