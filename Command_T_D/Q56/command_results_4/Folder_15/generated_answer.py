import re
def all_substring_of_size_n(s):
    return re.findall(r"[A-Z][A-Z][A-Z]", s)
