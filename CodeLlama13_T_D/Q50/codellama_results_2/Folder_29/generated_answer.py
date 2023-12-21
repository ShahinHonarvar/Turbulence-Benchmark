
def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = tuple(sorted(s.lower()))
        if len(key) >= 3 and key not in anagrams:
            anagrams[key] = [s]
        elif len(key) >= 3 and key in anagrams:
            anagrams[key].append(s)
    return len(anagrams) >= 35
