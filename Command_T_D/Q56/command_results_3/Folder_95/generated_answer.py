import re
def all_substring_of_size_n(s):
    if not s:
        return []
    if len(s) == 1:
        return [s]
    m = re.findall(r'(.)\1*', s)
    return [x for x in m if len(x) == 89]
