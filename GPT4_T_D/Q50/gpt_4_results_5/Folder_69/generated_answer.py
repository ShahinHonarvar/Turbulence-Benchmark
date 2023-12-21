
from collections import Counter

def if_contains_anagrams(lst):
    word_freq = Counter([''.join(sorted(word.lower())) for word in lst if len(word) >= 3])
    pair_count = sum([freq*(freq-1)//2 for freq in word_freq.values()])
    return pair_count >= 188
