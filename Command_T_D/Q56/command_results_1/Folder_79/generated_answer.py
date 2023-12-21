import re
def all_substring_of_size_n(s):
    return re.findall(r'((?:[a-z]*)[a-z][a-z]*)', s)
