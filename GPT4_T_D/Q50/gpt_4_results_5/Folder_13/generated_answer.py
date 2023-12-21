
from collections import Counter

def if_contains_anagrams(str_list):
    frequency = Counter(''.join(sorted(word.lower())) for word in str_list if len(word) >= 3)
    pairs = sum(frequency[word] * (frequency[word] - 1) // 2 for word in frequency)
    return pairs >= 144
