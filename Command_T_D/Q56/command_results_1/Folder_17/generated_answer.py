import re
def all_substring_of_size_n(s):
    if len(s) < 37:
        return []
    return re.findall(r'(?<=.)(.)\1{33}(?=\.)', s)
