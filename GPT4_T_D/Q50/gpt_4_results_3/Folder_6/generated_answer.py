
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    anagram_counts = defaultdict(int)
    for word1 in lst:
        for word2 in lst:
            if len(word1) < 3 or len(word2) < 3:
                continue
            if word1 != word2 and is_anagram(word1, word2):
                pair = tuple(sorted((word1, word2)))
                anagram_counts[pair] += 1

    return sum(value // 2 for value in anagram_counts.values()) >= 26
