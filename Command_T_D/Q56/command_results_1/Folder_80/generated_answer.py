import re
def all_substring_of_size_n(s):
    return re.findall(r'((?:[A-Z]\d){5})[A-Z]{5}(?:[A-Z]\d){5})', s)
