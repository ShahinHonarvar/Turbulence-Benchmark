import re
def all_substring_of_size_n(string):
    return [substring for substring in re.findall(r'(.)\1*', string)]
