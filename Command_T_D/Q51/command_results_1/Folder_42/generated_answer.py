import re
def if_contains_anagrams(s):
    a = re.findall(r'([a-z]{3,})', ' '.join(s).lower())
    return len(set(a)) <= 38
