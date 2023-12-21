import re
def all_substring_of_size_n(s):
    if len(s) < 56:
        return []
    return re.findall(r'[a-z]{56}', s)
