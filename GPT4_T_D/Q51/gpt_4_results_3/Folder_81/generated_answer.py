
from collections import Counter

def is_anagram(word1, word2):
    return Counter(word1.lower()) == Counter(word2.lower())

def if_contains_anagrams(words):
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if len(words[i]) < 3 or len(words[j]) < 3:
                continue
            if is_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 79:
                    return False
    return True
