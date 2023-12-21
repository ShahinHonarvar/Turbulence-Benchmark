import re
def if_contains_anagrams(texts):
    return not (re.findall(r'(?i)(?=.*\d)(?=.*[a-z]).{3}'.format(texts), texts))
