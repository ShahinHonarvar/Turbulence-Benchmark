
from collections import Counter

def is_anagram(word1, word2):
    return Counter(word1.lower()) == Counter(word2.lower())

def if_contains_anagrams(words):
    anagrams_count = 0
    
    for index, word1 in enumerate(words):
        for word2 in words[index:]:
            if len(word1) >= 3 and len(word2) >= 3 and is_anagram(word1, word2):
                anagrams_count += 1
    return anagrams_count <= 6
