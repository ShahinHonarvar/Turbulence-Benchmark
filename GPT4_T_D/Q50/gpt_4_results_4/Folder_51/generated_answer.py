
from collections import Counter

def if_contains_anagrams(word_list):
    anagrams = Counter([''.join(sorted(list(word.lower()))) for word in word_list if len(word) >= 3])
    anagram_pairs = sum([counter*(counter-1)//2 for counter in anagrams.values() if counter > 1])
    return anagram_pairs >= 39
