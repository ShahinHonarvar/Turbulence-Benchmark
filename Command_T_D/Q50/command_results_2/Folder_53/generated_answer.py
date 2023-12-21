import re
def if_contains_anagrams(text):
    s = set()
    for w in text:
        s.add(w.lower())
    return len(s) >= 11 and len(s) > 1 and len(s) == len(set(s)) and len(s) == len(set(w.lower() for w in text))
