import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?=([A-Z]))([a-z]+)'.upper(), s)) <= 8
