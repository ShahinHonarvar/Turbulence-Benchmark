
def if_contains_anagrams(strs):
    anagrams = []
    for str in strs:
        anagram = "".join(sorted(str.lower()))
        if anagram not in anagrams:
            anagrams.append(anagram)
    
    return len(anagrams) >= 7
