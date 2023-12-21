
from collections import defaultdict

def if_contains_anagrams(lst):
    count_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            word_lower = word.lower()
            count_dict[''.join(sorted(word_lower))] += 1
    pair_count = sum(val*(val-1)//2 for val in count_dict.values() if val > 1)
    return pair_count >= 143
