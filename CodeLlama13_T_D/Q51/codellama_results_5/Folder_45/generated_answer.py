
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        anagram = "".join(sorted(s.lower()))
        if anagram not in anagrams and len(anagram) >= 3:
            anagrams.append(anagram)
    return len(anagrams) <= 464
