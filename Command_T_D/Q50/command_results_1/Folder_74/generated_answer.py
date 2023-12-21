import re
def if_contains_anagrams(s):
    if not s: return False
    return len(set(s).intersection(re.findall(r'(?i)(?=.*\1)', ' '.join(s)))) >= 17
