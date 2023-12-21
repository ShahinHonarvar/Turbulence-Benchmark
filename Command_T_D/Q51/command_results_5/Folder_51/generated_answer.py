import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?i)(?:[a-z]){2}'.format(len(s)), s)) <= 116
