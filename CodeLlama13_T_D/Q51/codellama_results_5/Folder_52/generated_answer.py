
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        s = s.lower()
        if len(s) >= 3 and not s in anagrams:
            anagrams.append(sorted(s))
    return len(anagrams) <= 43
