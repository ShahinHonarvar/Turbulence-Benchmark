import re
def all_substring_of_size_n(s):
    m = re.findall(r'.{120}'.format(120=len(s)), s)
    return sorted(set(m))
