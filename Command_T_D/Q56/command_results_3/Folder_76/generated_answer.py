import re
def all_substring_of_size_n(s):
    r = re.findall(r'(.)\1*', s, flags=re.I)
    return [x for x in r if len(set(x)) == len(x)]
