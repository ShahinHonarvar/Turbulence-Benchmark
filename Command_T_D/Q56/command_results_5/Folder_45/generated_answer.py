import re
def all_substring_of_size_n(s):
    res = []
    for m in re.finditer(r'(.)\1+', s):
        if len(m.group()) == 29:
            res += [m.group()]
    return res
