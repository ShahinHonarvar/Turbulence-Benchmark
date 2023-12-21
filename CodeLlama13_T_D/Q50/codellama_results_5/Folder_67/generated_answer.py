
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        if len(s) < 3:
            continue
        normalized = "".join(sorted(s.lower()))
        if normalized not in anagrams:
            anagrams.add(normalized)
    return len(anagrams) >= 41
