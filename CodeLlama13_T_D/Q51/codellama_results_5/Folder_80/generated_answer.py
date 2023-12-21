
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        anagram = "".join(sorted(s))
        if len(anagram) >= 3 and anagram not in anagrams:
            anagrams.add(anagram)
    return len(anagrams) <= 255
