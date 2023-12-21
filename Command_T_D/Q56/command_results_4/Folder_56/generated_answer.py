import re
def all_substring_of_size_n(s):
    res = re.findall(r'(.)\1*', s, flags=re.I)
    return [a[0] for a in res]
