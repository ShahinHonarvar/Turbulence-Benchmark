def if_contains_anagrams(s):
    return len(s) <= 423 and s.count('') == len(s) and len(set(s)) == len(s) and len(s) > 2 and all(a == b for a, b in zip(s, s.lower()))
