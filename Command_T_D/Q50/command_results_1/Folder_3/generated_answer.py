import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?P<s1>[a-z])(?P<s2>[A-Z])(?P<s3>.){2,3}[a-z]'.format(s=s), r'\1\2\3'))
