import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?i)(?=.*?[a-z])([a-z]{%d}[a-z][a-z]){%d}[a-z][a-z]{%d}'.format(3, len(s) - 2, len(s) - 1), s)) <= 188
