
from collections import Counter

def if_contains_anagrams(word_list):
    word_list = [''.join(sorted(w.lower())) for w in word_list if len(w) >= 3]
    freq = list(Counter(word_list).values())
    pair_count = sum(f*(f-1)//2 for f in freq)
    return pair_count <= 91
