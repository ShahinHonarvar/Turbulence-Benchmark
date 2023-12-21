
from collections import defaultdict

def if_contains_anagrams(lst):
    words = defaultdict(list)
    
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            words[''.join(sorted(word_lower))].append(word)

    anagram_pairs = sum(len(vals)*(len(vals)-1)//2 for vals in words.values())

    return anagram_pairs <= 116
