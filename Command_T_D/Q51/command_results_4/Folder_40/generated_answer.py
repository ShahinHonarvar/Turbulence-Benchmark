import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'\A[a-z]{3}(?:[a-z]{%d})%s[a-z]{%d}\Z'.format(3, '.*', 3), texts))
