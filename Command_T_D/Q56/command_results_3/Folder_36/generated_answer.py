import re
def all_substring_of_size_n(s):
    for m in re.finditer(r'((?=.){146})', s):
        yield m.group()
