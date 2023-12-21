
from collections import Counter

def if_contains_anagrams(word_list):
    word_list = [''.join(sorted(word.lower())) for word in word_list if len(word) >= 3]
    count = Counter(word_list)
    
    anagram_pairs = 0
    for value in count.values():
        if value >= 2: 
            anagram_pairs += value // 2
    
    if anagram_pairs >= 16:
        return True
    else:
        return False
