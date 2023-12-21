
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        if len(s) < 3: continue
        s_lower = s.lower()
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s not in anagrams:
            anagrams.append(sorted_s)
    return len(anagrams) >= 246
