import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?i)(?=.*\1).*' + '.*'.join(re.findall(r'(?i)(?=.*\1).*', s)), s)) >= 22
