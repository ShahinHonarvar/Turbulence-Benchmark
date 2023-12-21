
from collections import Counter

def if_contains_anagrams(words):
    anagrams_counter = Counter(str(sorted(word.lower())) for word in words if len(word) >= 3)
    pairs_count = sum(v*(v-1)//2 for v in anagrams_counter.values())
    return pairs_count >= 140
