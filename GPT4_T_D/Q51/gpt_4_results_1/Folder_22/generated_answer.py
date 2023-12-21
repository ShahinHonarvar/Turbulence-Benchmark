
from collections import Counter
import itertools

def if_contains_anagrams(word_list):
    word_list = [''.join(sorted(word.lower())) for word in word_list if len(word) >= 3]
    anagrams = sum(1 for a, b in itertools.combinations(word_list, 2) if Counter(a) == Counter(b))
    if anagrams <= 14:
        return True
    else:
        return False
