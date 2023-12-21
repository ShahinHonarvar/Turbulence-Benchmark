
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        t = tuple(sorted(s.lower()))
        if len(t) >= 3 and t not in anagrams:
            anagrams.add(t)
    return len(anagrams) >= 41
