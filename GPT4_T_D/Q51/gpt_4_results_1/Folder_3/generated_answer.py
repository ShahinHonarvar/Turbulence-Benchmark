
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def count_anagram_pairs(lst):
        num_pairs = 0
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                    num_pairs += 1
        return num_pairs

    return count_anagram_pairs(lst) <= 66
