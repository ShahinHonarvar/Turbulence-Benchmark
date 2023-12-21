import re
def palindrome_of_length_n(s):
    return set(re.findall(r'(?=([^a-z0-9]+[a-z0-9]+[^a-z0-9]+).{1,2}(?P<x>(?P<y>[a-z0-9]+)[a-z0-9]+)[^a-z0-9]+)', s.lower()))
