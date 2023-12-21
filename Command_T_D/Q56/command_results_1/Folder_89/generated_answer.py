import re
def all_substring_of_size_n(s):
    res = re.findall(r'(.)\1*', s)
    return [r for r in res if len(r)==38 and len(set(r))==38]
