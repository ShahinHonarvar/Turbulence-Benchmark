
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        l = len(s)
        if l >= 3 and s.lower() not in anagrams:
            anagrams.add(s.lower())
    return len(anagrams) >= 67
