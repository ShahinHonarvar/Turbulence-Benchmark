
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3 and not key in anagrams:
            anagrams.append(key)
    return len(anagrams) <= 18
