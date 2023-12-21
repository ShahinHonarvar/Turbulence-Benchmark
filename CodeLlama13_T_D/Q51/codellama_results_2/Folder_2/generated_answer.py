
def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        lowercase = string.lower()
        anagram = ''.join(sorted(lowercase))
        if anagram not in anagrams:
            anagrams.append(anagram)
    return len(anagrams) <= 81
