
from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    # store sorted words
    sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]

    # count sorted words
    counts = Counter(sorted_words)

    # count pairs of anagrams
    anagram_pairs = sum(val*(val-1)//2 for val in counts.values())

    # return whether there are at most 366 pairs of anagrams
    return anagram_pairs <= 366
