
from collections import Counter

def if_contains_anagrams(strings):
    anagram_counter = 0
    anagram_dict = {}
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
        
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            anagram_counter += len(anagram_dict[key])*(len(anagram_dict[key])-1) // 2
            
    return anagram_counter <= 85
