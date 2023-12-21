def if_contains_anagrams(s):
    return not set(s).intersection(set(a for a in s if len(a) >= 3)).intersection(set(b for b in s if len(b) >= 3))
