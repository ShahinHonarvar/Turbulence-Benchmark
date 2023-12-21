
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3 and s_lower not in anagrams:
            anagrams.add(s_lower)
            anagrams.update(''.join(sorted(c)) for c in s_lower)
    return len(anagrams) <= 407
