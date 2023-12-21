
from collections import Counter

def if_contains_anagrams(words_list):
    frequency_map = Counter([''.join(sorted(word.lower())) for word in words_list if len(word) >= 3])
    
    pairs = sum(it*(it-1)//2 for it in frequency_map.values())
    
    return pairs >= 79
