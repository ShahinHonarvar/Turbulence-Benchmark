
from itertools import combinations
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())

    anagram_count = 0
    for word1, word2 in combinations(lst, 2):
        if len(word1) > 2 and len(word2) > 2 and is_anagram(word1, word2):
            anagram_count += 1
        if anagram_count >= 85:
            return True
    return False
