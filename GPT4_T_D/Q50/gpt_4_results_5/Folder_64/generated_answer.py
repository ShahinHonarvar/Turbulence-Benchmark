
from collections import Counter

def if_contains_anagrams(lst):
    sorted_lst = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counts = list(Counter(sorted_lst).values())
    return sum(i for i in counts if i > 1) >= 5
