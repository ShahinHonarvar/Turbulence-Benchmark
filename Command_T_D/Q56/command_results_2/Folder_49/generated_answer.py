import re
def all_substring_of_size_n(s):
    return re.findall(r'(\S){73}(\S)', s)
