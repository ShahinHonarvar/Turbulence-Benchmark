
from collections import defaultdict

def if_contains_anagrams(lst):
    
    ana_count = 0
    word_dict = defaultdict(list)
    
    for word in lst:
        word_dict[str(sorted(word.lower()))] += [word]
    
    for key in word_dict.keys():
        if len(key) >= 3 and len(word_dict[key]) > 1:
            ana_count += len(word_dict[key])*(len(word_dict[key]) - 1) // 2
    
    return ana_count >= 277
