
from collections import defaultdict

def if_contains_anagrams(strings_list):
    anagram_pairs = defaultdict(list)
    anagram_count = 0

    for word in strings_list:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_pairs[sorted_word].append(word)
    
    for words in anagram_pairs.values():
        if len(words) > 1:
            anagram_count += len(words) * (len(words) - 1) // 2
            
    return anagram_count <= 401
