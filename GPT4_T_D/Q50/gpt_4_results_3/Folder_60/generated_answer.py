
from collections import Counter
from itertools import combinations

def if_contains_anagrams(words_list):
    words_list = ["".join(sorted(word.lower())) for word in words_list if len(word) >= 3]
    counter = Counter(words_list)
    anagrams = [value for value in counter.values() if value > 1]
    pairs = sum([comb for n in anagrams for comb in combinations(range(n), 2)])

    if pairs >= 60:
        return True
    else:
        return False
