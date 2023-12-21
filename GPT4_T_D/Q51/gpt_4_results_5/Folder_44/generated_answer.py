
from collections import defaultdict

def if_contains_anagrams(lst):
    words_dict = defaultdict(list)
    
    for word in lst:
        words_dict[''.join(sorted(word.lower()))].append(word)
    
    pair_count = 0
    for anagrams in words_dict.values():
        if len(anagrams) > 1 and len(anagrams[0]) >= 3:
            pair_count += len(anagrams) * (len(anagrams) - 1) / 2
            if pair_count > 75:
                return False
    
    return True
