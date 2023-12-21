
def if_contains_anagrams(strs):
    anagrams = set()
    for s in strs:
        normalized = ''.join(sorted(s.lower()))
        if normalized not in anagrams and len(normalized) >= 3:
            anagrams.add(normalized)
    return len(anagrams) >= 30
