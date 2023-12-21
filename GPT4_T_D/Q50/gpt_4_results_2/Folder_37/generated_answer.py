
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(list(word.lower())))
            anagrams.append(sorted_word)
    counts = Counter(anagrams)
    return sum(1 for key in counts if counts[key] > 1) >= 29
