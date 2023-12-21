
from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)
            
    count = 0
    for word, anagrams in anagram_dict.items():
        if len(anagrams) > 1:
            count += 1
            
    return count >= 26
