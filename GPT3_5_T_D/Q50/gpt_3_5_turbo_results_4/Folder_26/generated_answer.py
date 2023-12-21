
from collections import defaultdict

def if_contains_anagrams(strings):
    def get_key(word):
        return ''.join(sorted(word.lower()))
    
    anagrams = defaultdict(int)
    
    for word in strings:
        if len(word) >= 3:
            key = get_key(word)
            anagrams[key] += 1
    
    count = 0
    for key in anagrams:
        count += anagrams[key] * (anagrams[key]-1) // 2
    
    return count >= 49
