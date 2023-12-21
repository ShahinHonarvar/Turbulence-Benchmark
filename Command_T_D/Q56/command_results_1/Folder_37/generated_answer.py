import re
def all_substring_of_size_n(s):
    return re.findall(r'[a-z]{65}'.format(65), s)
