
from collections import defaultdict

def check_if_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if check_if_anagram(lst[i], lst[j]):
                    anagram_count += 1
            if anagram_count > 84:
                return False
    return True
