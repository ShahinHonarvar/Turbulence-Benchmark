import re
def all_substring_of_size_n(s):
    m = re.finditer(r'.{1,144}', s)
    return [m.group() for m in m if m.group() not in s]
