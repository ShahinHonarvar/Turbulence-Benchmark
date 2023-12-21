
from collections import Counter

def if_contains_anagrams(lst):
    sorted_list = [''.join(sorted(e.lower())) for e in lst if len(e) >= 3]
    count = Counter(sorted_list)
    pair_count = 0
    for k,v in count.items():
        pair_count += v*(v-1)//2 # Identify pairs of anagrams
    if pair_count > 35:
        return False
    return True
