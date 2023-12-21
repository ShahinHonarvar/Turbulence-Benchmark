
from collections import Counter

def if_contains_anagrams(lst):
    def count_anagrams(lst):
        sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
        counter = Counter(sorted_words)
        return sum(v * (v - 1) // 2 for v in counter.values())
    
    return count_anagrams(lst) <= 22
