
from collections import Counter

def if_contains_anagrams(string_list):
    word_freq = Counter([''.join(sorted(word.lower())) for word in string_list if len(word) >= 3])
    pairs_count = sum(val * (val - 1) // 2 for val in word_freq.values() if val > 1)
    return pairs_count >= 312
