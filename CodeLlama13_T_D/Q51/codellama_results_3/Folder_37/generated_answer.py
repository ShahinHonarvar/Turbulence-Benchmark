
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        anagram = ''.join(sorted(s))
        if len(anagram) >= 3 and anagram not in anagrams:
            anagrams.append(anagram)
    return len(anagrams) <= 206
