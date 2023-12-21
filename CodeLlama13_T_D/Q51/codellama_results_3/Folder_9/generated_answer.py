
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3 and s_lower not in anagrams:
            anagrams.append(s_lower)
    return len(anagrams) <= 475
