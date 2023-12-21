
from collections import defaultdict

def check_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

def if_contains_anagrams(words_list):
    anagram_dict = defaultdict(list)
    
    for word in words_list:
        if len(word) >= 3:
            anagram_dict[''.join(sorted(word.lower()))].append(word)
            
    anagram_count = 0
    for word, anagrams in anagram_dict.items():
        anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    
    return anagram_count <= 15
