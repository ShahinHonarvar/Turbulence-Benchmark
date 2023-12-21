import re
def all_substring_of_size_n(string):
    match = re.findall(r'(.)\1*', string, flags=re.I)
    return match
