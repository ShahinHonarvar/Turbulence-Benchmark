
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        ls = sorted(s.lower())
        if len(ls) >= 3 and ls not in anagrams:
            anagrams.add(ls)
    return len(anagrams) <= 61
