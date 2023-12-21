import re
def all_substring_of_size_n(s):
    for m in re.finditer(r'<[a-z]{1,60}>', s):
        yield m.group()
