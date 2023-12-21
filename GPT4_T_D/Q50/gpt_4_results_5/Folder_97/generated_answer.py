
from collections import Counter

def if_contains_anagrams(lst):
    str_dict = {}
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = "".join(sorted(word_lower))
            if sorted_word in str_dict:
                str_dict[sorted_word].append(word_lower)
            else:
                str_dict[sorted_word] = [word_lower]
                
    pairs_count = sum([val*(val-1)//2 for val in Counter([len(lst) for lst in str_dict.values()]).values()])
    if pairs_count >= 123:
        return True
    else:
        return False
