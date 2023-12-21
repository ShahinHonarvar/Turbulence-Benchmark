
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)
    pairs = sum(len(words)*(len(words)-1)//2 for words in anagrams.values())
    return pairs <= 69
