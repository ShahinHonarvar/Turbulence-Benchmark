import re
def all_substring_of_size_n(string):
    if not string:
        return []
    if len(string) < 79:
        return []
    return re.findall(r'[A-z0-9]+', string, flags=re.I)
