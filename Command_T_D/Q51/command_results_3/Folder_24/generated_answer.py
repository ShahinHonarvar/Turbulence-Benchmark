import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?P<s1>[a-z]{3})(?P<s2>[a-z]{%d})(?P<s3>[a-z]{%d})'.format(3, 3), s))
