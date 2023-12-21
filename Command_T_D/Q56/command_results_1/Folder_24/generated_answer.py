import re
def all_substring_of_size_n(string):
    if not string:
        return []
    res = re.findall(r'(.)\1*', string)
    return [s for s in res if len(s) == 52]
