
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3: continue
        anagram = ''.join(sorted(s_lower))
        if anagram not in anagrams:
            anagrams.add(anagram)
    return len(anagrams) <= 25
