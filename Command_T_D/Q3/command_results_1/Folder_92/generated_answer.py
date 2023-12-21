import re
def all_pos_ints_inclusive(lst):
    if not lst:
        return []
    reg_ex = re.compile('(?<=[0-9])0*(?=[1-9][0-9]*)')
    return [x for x in range(0, len(lst) + 1) if reg_ex.match(str(x)) and x > 0]
