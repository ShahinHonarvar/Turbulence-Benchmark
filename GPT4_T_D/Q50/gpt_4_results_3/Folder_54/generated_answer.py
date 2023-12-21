
from collections import Counter

def if_contains_anagrams(str_list):
    anagram_counts = Counter()
    for word in str_list:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            anagram_counts[sorted_word] += 1
    
    pair_counts = sum([x * (x-1) // 2 for x in anagram_counts.values()])
    
    return pair_counts >= 74
