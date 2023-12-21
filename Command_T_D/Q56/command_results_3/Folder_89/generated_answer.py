import re
def all_substring_of_size_n(string):
    return re.findall(r'([a-zA-Z0-9])+', string)
