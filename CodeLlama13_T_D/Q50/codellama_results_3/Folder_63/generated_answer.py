
def if_contains_anagrams(strs):
    anagrams = set()
    for s in strs:
        if len(s) < 3: continue
        lower = s.lower()
        sorted_chars = "".join(sorted(lower))
        if sorted_chars not in anagrams:
            anagrams.add(sorted_chars)
    return len(anagrams) >= 89
