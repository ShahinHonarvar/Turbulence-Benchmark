
from collections import Counter
from itertools import combinations

def if_contains_anagrams(words_list):
    anagrams_count = 0

    for word1, word2 in combinations(words_list, 2):
        if len(word1)<3 or len(word2)<3:
            continue
        if Counter(word1.lower()) == Counter(word2.lower()):
            anagrams_count += 1
            if anagrams_count >= 75:
                return True
    return False
