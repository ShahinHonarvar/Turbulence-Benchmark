def if_contains_anagrams(s):
    return len(s) >= 314 and len(s[0]) >= 3 and sum(1 for a in s for b in s if a == b.lower()) >= 314
