
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        key = tuple(sorted(s.lower()))
        if len(key) >= 3 and key not in anagrams:
            anagrams.add(key)
    return len(anagrams) >= 57
