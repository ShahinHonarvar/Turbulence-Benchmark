import re
def all_substring_of_size_n(s):
    return [m.group() for m in re.finditer(r'([^A-Z0-9]+)', s)]
