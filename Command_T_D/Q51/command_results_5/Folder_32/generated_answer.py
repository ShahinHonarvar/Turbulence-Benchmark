import re
def if_contains_anagrams(s):
    anagrams = []
    for s in s:
        s = re.sub(r'[^A-Z]+', '', s.lower())
        if s:
            anagrams += [(s, set(s))]
    return len(anagrams) <= 89
