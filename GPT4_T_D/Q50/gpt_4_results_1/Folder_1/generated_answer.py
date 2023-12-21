
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []

    for word in lst:
        if len(word) >= 3:
            anagrams.append(''.join(sorted(list(word.lower()))))

    counter = Counter(anagrams)
    pair_count = 0

    for word in counter:
        if counter[word] > 1:
            pair_count += counter[word]//2

    if pair_count >= 96:
        return True
    else:
        return False
