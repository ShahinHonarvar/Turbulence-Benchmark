
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_groups = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_groups[sorted_word].append(word)
    pairs_counter = 0
    for group in anagram_groups.values():
        n = len(group)
        pairs_counter += n * (n - 1) / 2
        if pairs_counter > 74:
            return False
    return True
