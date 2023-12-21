
from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)

    pair_count = 0
    for val in anagrams.values():
        pair_count = pair_count + len(val) // 2

    if pair_count >= 10:
        return True
    else:
        return False
