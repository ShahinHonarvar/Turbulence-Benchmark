
def if_contains_anagrams(lst):
    letter_anagrams = {}
    anagram_pairs = 0
    
    for string in lst:
        string = string.lower()
        letters = ''.join(sorted(string))
        
        if len(string) >= 3:
            if letters in letter_anagrams:
                letter_anagrams[letters] += 1
            else:
                letter_anagrams[letters] = 1
    
    for count in letter_anagrams.values():
        anagram_pairs += count * (count - 1) // 2
    
    return anagram_pairs <= 116
