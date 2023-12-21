
def if_contains_anagrams(strs):
    anagrams = set()
    for s in strs:
        key = tuple(sorted(s.lower()))
        if len(key) >= 3 and key not in anagrams:
            anagrams.add(key)
    return len(anagrams) <= 24
