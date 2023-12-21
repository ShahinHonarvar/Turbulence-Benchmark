import re
def all_substring_of_size_n(string):
    return re.findall(r'([\w]+){48}', string)
