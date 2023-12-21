
def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            anagram = "".join(sorted(string))
            if anagram not in anagrams:
                anagrams.append(anagram)
    
    return len(anagrams) >= 140
