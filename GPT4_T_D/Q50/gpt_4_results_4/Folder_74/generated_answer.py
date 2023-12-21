
from collections import Counter

def if_contains_anagrams(lst):
    # Create Counter for string representations of sorted words
    word_counters = Counter(''.join(sorted(word.lower())) for word in lst if len(word) >= 3)
    
    # Count pairs of anagrams
    pair_count = sum(count * (count - 1) // 2 for count in word_counters.values())

    return pair_count >= 17
