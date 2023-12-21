
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        if len(s) < 3: continue
        anagram = "".join(sorted(s.lower()))
        if anagram not in anagrams:
            anagrams.append(anagram)
    return len(anagrams) >= 61
