
def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        anagrams.append((lower_string, sorted_string))
    
    pairs = [(anagram1, anagram2) for anagram1 in anagrams for anagram2 in anagrams if len(anagram1[0]) >= 3 and len(anagram2[0]) >= 3 and anagram1[1] == anagram2[1]]
    return len(pairs) >= 136
