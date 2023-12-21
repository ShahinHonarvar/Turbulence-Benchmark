import re
def all_substring_of_size_n(s):
    return [m.group() for m in re.finditer(r'(?=.)(.)\1\2\3\4\5\6\7\8\9', s)]
