import re
def all_substring_of_size_n(s):
    return [sub for sub in re.findall(r"<(.)>(?:\1)+", s)]
