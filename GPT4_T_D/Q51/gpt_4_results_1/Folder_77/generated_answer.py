
from collections import defaultdict 

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    anagram_pairs = 0
    dictionary = defaultdict(list)

    for s in lst:
        if len(s) >= 3:
            sorted_word = ''.join(sorted(s.lower()))
            dictionary[sorted_word].append(s)
    
    for word, duplicates in dictionary.items():
        if len(duplicates) > 1:
            anagram_pairs += len(duplicates) // 2
  
    return anagram_pairs <= 17
