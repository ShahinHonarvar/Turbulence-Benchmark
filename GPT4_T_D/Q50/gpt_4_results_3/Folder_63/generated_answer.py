
from collections import Counter

def if_contains_anagrams(str_list):
    sorted_strings = [''.join(sorted(s.lower())) for s in str_list if len(s) >= 3]
    count = Counter(sorted_strings)
    pairs = sum(v*(v-1)//2 for v in count.values())
    return pairs >= 89
