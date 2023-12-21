
from collections import Counter

def if_contains_anagrams(words):
    anagrams = Counter()
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word] += 1

    pair_count = sum((count * (count - 1)) // 2 for count in anagrams.values())
    
    return pair_count <= 36
