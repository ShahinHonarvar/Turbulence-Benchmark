
from collections import defaultdict

def if_contains_anagrams(str_list):
    str_list = [word.lower() for word in str_list if len(word) >= 3]
    anagram_dict = defaultdict(list)
    
    for word in str_list:
        sorted_word = "".join(sorted(word))
        anagram_dict[sorted_word].append(word)
        
    anagram_pairs = 0
    for anagram_list in anagram_dict.values():
        no_of_words = len(anagram_list)
        if no_of_words > 1:
            anagram_pairs += no_of_words * (no_of_words - 1) // 2
        if anagram_pairs >= 188:
            return True

    return False
