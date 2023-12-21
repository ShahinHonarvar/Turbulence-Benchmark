
from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())

    anagrams = 0
    for pair in combinations(lst, 2):
        if len(pair[0]) >= 3 and len(pair[1]) >= 3 and is_anagram(*pair):
            anagrams += 1

    return anagrams <= 206
