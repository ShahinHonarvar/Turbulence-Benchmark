
from collections import Counter

def if_contains_anagrams(strings):
    str_list = [''.join(sorted(s.lower())) for s in strings 
                if len(s) >= 3]
    freq_count = Counter(str_list)
    pairs = sum(v*(v-1)//2 for v in freq_count.values())
    return pairs >= 58
