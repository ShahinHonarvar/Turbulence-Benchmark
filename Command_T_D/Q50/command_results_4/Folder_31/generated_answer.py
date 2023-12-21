def if_contains_anagrams(s):
    return (3 <= len(s) and s.lower() and len(s) - len(set(s)) >= 68)
