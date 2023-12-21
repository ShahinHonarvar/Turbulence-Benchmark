
from collections import defaultdict

def if_contains_anagrams(lst):
    word_dict = defaultdict(set)
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            word_dict[''.join(sorted(word_lower))].add(word_lower)
    
    count = sum(len(values) * (len(values) - 1) // 2 for values in word_dict.values())

    return count <= 173
