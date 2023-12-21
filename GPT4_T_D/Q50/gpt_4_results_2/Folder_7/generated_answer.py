
from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [''.join(sorted(s.lower())) for s in str_list if len(s) >= 3]
    counter = Counter(str_list)
    total_pairs = sum(v*(v-1)//2 for k,v in counter.items())
    return total_pairs >= 178
