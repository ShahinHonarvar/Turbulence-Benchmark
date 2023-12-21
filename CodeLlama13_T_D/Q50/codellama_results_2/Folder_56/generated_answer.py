
def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) < 3:
            continue
        if key not in anagrams:
            anagrams[key] = 1
        else:
            anagrams[key] += 1
    return sum(anagrams.values()) >= 77
