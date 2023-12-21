
from collections import Counter

def if_contains_anagrams(str_list):
    str_counter = Counter([''.join(sorted(s.lower())) for s in str_list if len(s) >= 3])
    pair_count = sum([count*(count-1)//2 for count in str_counter.values()])
    return pair_count >= 73
