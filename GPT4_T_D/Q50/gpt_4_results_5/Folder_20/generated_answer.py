
from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    anagrams_count = 0
    count_map = ["".join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counter = Counter(count_map)
    for value in counter.values():
        if value > 1:
            anagrams_count += sum([1 for combo in combinations(range(value), 2)])

    return anagrams_count >= 64
