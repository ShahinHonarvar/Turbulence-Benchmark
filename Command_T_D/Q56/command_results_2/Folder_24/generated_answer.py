import re
def all_substring_of_size_n(string):
    return [re.sub(r'(.)\1+', r'\1', s) for s in re.findall(r'(.)\1*', string)]
