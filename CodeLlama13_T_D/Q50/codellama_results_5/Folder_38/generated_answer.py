
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        key = tuple(sorted(s.lower()))
        if key not in anagrams:
            anagrams.append(key)
    return len(anagrams) >= 24
