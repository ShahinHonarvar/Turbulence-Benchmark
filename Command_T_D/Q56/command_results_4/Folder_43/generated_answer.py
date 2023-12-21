import re
def all_substring_of_size_n(s):
    return [m.group() for m in re.finditer(r'(?=({}){86}({}))'.format(r'[a-z]', re.escape(s)), s)]
