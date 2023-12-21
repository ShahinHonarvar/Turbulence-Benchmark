
from collections import Counter

def if_contains_anagrams(word_list):
    tuples = [tuple(sorted(word.lower())) for word in word_list if len(word) >= 3]
    counter = Counter(tuples)
    pairs = sum([v*(v-1)//2 for v in counter.values()])
    return pairs <= 173
