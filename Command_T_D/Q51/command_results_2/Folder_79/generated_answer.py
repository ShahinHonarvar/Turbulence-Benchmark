import re
def if_contains_anagrams(s):
    return not (set(re.findall(r'(?i)([a-z])\1+', ''.join(s)) - set('aaa'))
