import re
def all_substring_of_size_n(s):
    for m in re.finditer(r'(.)\1+', s):
        yield m.group()
