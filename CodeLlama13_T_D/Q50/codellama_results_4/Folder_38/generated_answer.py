
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) < 3: continue
        anagram = ''.join(sorted(lower_s))
        if anagram not in anagrams:
            anagrams.add(anagram)
    return len(anagrams) >= 24
