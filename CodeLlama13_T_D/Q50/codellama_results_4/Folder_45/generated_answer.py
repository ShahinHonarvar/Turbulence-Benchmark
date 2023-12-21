
def if_contains_anagrams(strs):
    anagrams = set()
    for s in strs:
        if len(s) >= 3 and s.lower() not in anagrams:
            anagrams.add(tuple(sorted(s)))
    return len(anagrams) >= 277
