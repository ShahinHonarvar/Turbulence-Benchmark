
from collections import Counter

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i].lower(), lst[j].lower()):
                anagram_pairs += 1
    return anagram_pairs <= 66
