
def if_contains_anagrams(lst):
    anagrams = []
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) < 3: continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted not in anagrams:
            anagrams.append(s_sorted)
    return len(anagrams) >= 95
