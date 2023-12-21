
from collections import Counter

def if_contains_anagrams(str_list):

    sorted_strs = [''.join(sorted(w.lower())) for w in str_list if len(w) >= 3]
    count = Counter(sorted_strs)

    pairs = sum(v * (v - 1) // 2 for v in count.values())
    
    return pairs <= 255
