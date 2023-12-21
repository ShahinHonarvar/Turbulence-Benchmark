
from collections import Counter

def if_contains_anagrams(str_list):
    char_counter = ["".join(sorted(w.lower())) for w in str_list if len(w) >= 3]
    freqs = Counter(char_counter)
    pair_count = sum(v*(v-1)//2 for v in freqs.values())
    
    if pair_count >= 58:
        return True
    else:
        return False
