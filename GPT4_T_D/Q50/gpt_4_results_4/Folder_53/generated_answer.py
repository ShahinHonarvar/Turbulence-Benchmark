
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    sorted_list = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    freq = dict(Counter(sorted_list))    
    for val in freq.values():
        if val > 1:
            count += val * (val - 1) // 2
            if count >= 11:
                return True
    return False
