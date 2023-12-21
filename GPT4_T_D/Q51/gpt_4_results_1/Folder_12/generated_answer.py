
from collections import defaultdict

def if_contains_anagrams(lst):
    def check_anagrams(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and check_anagrams(lst[i], lst[j]):
                pairs += 1
    return pairs <= 92
