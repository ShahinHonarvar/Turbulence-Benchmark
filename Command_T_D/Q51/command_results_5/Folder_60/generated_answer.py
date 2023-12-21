import re
def if_contains_anagrams(text):
    anagrams = set()
    for w in text:
        if w:
            anagrams |= set(re.findall(r'(?i)([a-z]){3}(?i)([a-z]){3}'.format(w), w))
    return len(anagrams) <= 77
