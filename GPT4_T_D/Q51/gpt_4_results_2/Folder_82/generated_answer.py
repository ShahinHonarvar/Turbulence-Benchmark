
from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    anagram_count = 0
    sorted_hash_map = defaultdict(list)
    for i in lst:
        if len(i) >= 3:
            sorted_hash_map["".join(sorted(i.lower()))].append(i)

    for val in sorted_hash_map.values():
        if len(val) >= 2:
            pairs = combinations(val, 2)
            for pair in pairs:
                if is_anagram(*pair):
                    anagram_count += 1

    return anagram_count <= 40
