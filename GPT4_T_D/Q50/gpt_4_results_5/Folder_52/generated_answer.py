
from collections import Counter

def if_contains_anagrams(strings):
    strings = [x.lower() for x in strings if len(x) >= 3]
    anagrams_count = sum(Counter([''.join(sorted(word)) for word in strings]).values())
    return anagrams_count >= 58
