
from collections import Counter

def if_contains_anagrams(lst):
    count_pairs = 0
    sorted_lst = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counter = Counter(sorted_lst)
    
    for value in counter.values():
        count_pairs += value * (value - 1) // 2

    if count_pairs >= 97:
        return True
    else:
        return False
