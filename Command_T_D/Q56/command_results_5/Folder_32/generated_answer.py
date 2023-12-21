import re
def all_substring_of_size_n(s):
    res = []
    for match in re.finditer(r'(?=.)\w+', s):
        res.extend(match.group().split())
    return res
