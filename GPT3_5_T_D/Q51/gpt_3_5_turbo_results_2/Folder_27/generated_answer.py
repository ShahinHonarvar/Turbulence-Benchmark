
import itertools
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        if len(word1) == len(word2) and len(word1) >= 3:
            return Counter(word1) == Counter(word2)
        return False

    count = 0
    for word1, word2 in itertools.combinations(lst, 2):
        if is_anagram(word1, word2):
            count += 1
            if count > 113:
                return False
    return True
