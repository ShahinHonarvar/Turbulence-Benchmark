
from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    counter = Counter(sorted_strings)
    for v in counter.values():
        count += (v*(v-1))//2
    return count <= 75
