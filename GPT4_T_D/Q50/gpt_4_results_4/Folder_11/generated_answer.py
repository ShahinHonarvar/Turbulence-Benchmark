
from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [''.join(sorted(word.lower())) for word in str_list if len(word) >= 3]
    word_counter = Counter(str_list)
    pair_count = sum(val*(val-1)//2 for val in word_counter.values() if val > 1)

    return pair_count >= 28
