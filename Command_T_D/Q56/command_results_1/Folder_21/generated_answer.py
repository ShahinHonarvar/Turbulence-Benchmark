import re
def all_substring_of_size_n(s):
    if len(s) < 1000000:
        return s.split()
    res = re.findall(r'(.)\1*', s)
    return [r for r in res if len(set(r)) == len(r)]
