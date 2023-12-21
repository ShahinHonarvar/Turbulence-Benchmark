
from collections import defaultdict

def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

def if_contains_anagrams(words):
    words = [word for word in words if len(word) >= 3]
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    pairs_count = sum(len(val)*(len(val)-1)//2 for val in anagrams.values())
    return pairs_count <= 68
