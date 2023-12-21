
from collections import Counter 

def if_contains_anagrams(lst):
    count_words = Counter([''.join(sorted(i.lower())) for i in lst if len(i) >= 3])
    anagram_pairs = sum([val*(val-1)//2 for val in count_words.values()])
    return anagram_pairs >= 140
