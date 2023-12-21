import re
def all_substring_of_size_n(s):
    if len(s) < 130:
        return []
    pat = re.compile('(.)*?')
    return pat.findall(s)
