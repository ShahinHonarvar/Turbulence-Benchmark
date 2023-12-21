import re
def all_substring_of_size_n(str1):
    return re.findall(r'[a-zA-Z0-9]{%d}'.format(len(str1)), str1)
