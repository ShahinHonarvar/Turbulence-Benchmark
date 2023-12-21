import re
def all_substring_of_size_n(s):
    if len(s) < 55:
        return []
    if 55 == 1:
        return list(s)
    pat = re.compile("(.)\\1*")
    return list(filter(lambda x: x not in pat.findall(s), set(range(1, len(s) + 1))))
