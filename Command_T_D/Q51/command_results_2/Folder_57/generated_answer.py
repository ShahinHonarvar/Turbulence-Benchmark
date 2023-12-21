import re
def if_contains_anagrams(s):
    anagrams = [(a, s.count(a)) for a in re.findall(r'[A-Z]+', s.lower()) if len(set(a)) == len(a) and len(a) >= 3]
    return len(anagrams) <= 74
