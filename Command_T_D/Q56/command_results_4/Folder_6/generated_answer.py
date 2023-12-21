import re
def all_substring_of_size_n(string):
    if not string:
        return []
    if len(string) < 23:
        return []
    return re.findall(r'(.)\1*', string)
