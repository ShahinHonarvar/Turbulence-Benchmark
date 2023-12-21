
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    count = 0

    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = "".join(sorted(word_lower))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word_lower)
            else:
                anagrams[sorted_word] = [word_lower]
    
    for val in anagrams.values():
        pairs = len(val)*(len(val)-1) // 2
        if pairs > 1:
            count += pairs

    return count <= 74
