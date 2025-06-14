
def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3 and not any(string.lower() in s for s in anagrams):
            anagrams.append(string)
    return len(anagrams) >= 58
