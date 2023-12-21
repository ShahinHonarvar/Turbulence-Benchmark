
from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(set)
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].add(word)
        
    counter = 0
    for anagram_set in anagrams.values():
        size = len(anagram_set)
        if size > 1:
            counter += size*(size - 1) // 2

    return counter >= 92
