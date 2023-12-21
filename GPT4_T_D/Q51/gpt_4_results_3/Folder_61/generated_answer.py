
from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        word = word.lower()
        sorted_word = "".join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
                
    anagram_count = 0
    for value in anagram_dict.values():
        if len(value) > 1:
            anagram_count = anagram_count + (len(value) * (len(value) - 1)) // 2
            
    return anagram_count <= 50
