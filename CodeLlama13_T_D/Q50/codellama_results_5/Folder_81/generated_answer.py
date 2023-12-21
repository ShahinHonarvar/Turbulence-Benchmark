
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        if len(s) >= 3 and s.lower() not in anagrams:
            anagrams.add(tuple(sorted(s)))
    return len(anagrams) >= 16
