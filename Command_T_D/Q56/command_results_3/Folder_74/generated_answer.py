import re
def all_substring_of_size_n(s):
    if len(s) < 97:
        return []
    return sorted(re.findall(r'([\w]+){97}', s))
