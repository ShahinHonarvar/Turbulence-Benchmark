
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        if len(s) < 3: continue
        key = "".join(sorted(s.lower()))
        if key not in anagrams: anagrams.add(key)
    return len(anagrams) >= 140
