import re
def all_pos_ints_inclusive(integers):
    return [x for x in integers if re.fullmatch(r'[0-9]+', str(x))]
