
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        if len(word) < 3:
            continue
        temp_a = [''.join(sorted(word.lower()))]
        if temp_a not in anagrams:
            anagrams.append(temp_a)

    pairs = sum([counter * (counter - 1) / 2 for counter in Counter(i[0] for i in anagrams).values()])

    if pairs > 69:
        return False

    return True
