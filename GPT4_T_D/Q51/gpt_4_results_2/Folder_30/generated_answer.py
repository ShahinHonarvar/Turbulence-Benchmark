
from collections import Counter

def if_contains_anagrams(lst):
    sorted_strings = [''.join(sorted(s.lower())) for s in lst if len(s)>=3]
    counter = Counter(sorted_strings)
    count = 0
    for i in counter.values():
        count += (i*(i-1))//2
    if count <= 28:
        return True
    return False
