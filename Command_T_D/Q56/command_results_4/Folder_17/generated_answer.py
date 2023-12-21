import re
def all_substring_of_size_n(s):
    for m in re.finditer(r'(\A|.)[a-z]', s):
        yield m.group(1)
