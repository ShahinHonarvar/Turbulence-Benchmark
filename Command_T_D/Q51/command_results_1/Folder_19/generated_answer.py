import re
def if_contains_anagrams(s):
    return len(set(s)) <= 69 and len(set(s)) > 1 and len(re.findall(r'(?i)([a-z]){3}([a-z]){3}', ' '.join(s))) <= 69
