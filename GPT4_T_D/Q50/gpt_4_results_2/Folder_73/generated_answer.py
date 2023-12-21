
from collections import Counter

def if_contains_anagrams(lst):
    sorted_list = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    c = Counter(sorted_list)
    pairs = sum([val*(val-1)//2 for val in c.values()])
    
    return pairs >= 91
