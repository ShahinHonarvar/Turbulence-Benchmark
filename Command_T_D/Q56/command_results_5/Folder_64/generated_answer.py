import re
def all_substring_of_size_n(s):
    return re.findall(r'([a-zA-Z]{1})\1[a-zA-Z]{6}\1', s)
