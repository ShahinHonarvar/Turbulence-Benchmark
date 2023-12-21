import re
def all_substring_of_size_n(str1):
    str1 = str(str1)
    patterns = ['[a-z]{%d}' % 6]
    if re.search(patterns, str1):
        res = re.findall(patterns, str1)
        return res
    else:
        return []
