
from collections import Counter

def if_contains_anagrams(str_list):
    counter = 0
    anagram_list = [''.join(sorted(w.lower())) for w in str_list if len(w) >= 3]
    anagram_count = dict(Counter(anagram_list))
    for v in anagram_count.values():
        if v > 1:
            counter += v*(v-1) // 2
        if counter > 366:
            return False
    return True
