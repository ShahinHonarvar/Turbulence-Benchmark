
from collections import Counter

def if_contains_anagrams(word_list):
    counts = Counter([''.join(sorted(word.lower())) for word in word_list if len(word) >= 3])
    pairs = sum([count // 2 for count in counts.values()])
    
    return pairs >= 20
