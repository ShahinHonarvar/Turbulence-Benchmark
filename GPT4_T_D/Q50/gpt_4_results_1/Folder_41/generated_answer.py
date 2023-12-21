
from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [''.join(sorted(word.lower())) for word in str_list if len(word)>=3]
    counter = Counter(str_list)
    pair_num = sum([val*(val-1)//2 for val in counter.values()])
    return pair_num >= 75
