
from collections import Counter

def if_contains_anagrams(lst):
    word_count = Counter([''.join(sorted(word.lower())) for word in lst if len(word) >= 3])
    anagram_pairs = sum(v*(v-1)//2 for v in word_count.values())
    return anagram_pairs <= 257
