
from collections import Counter

def if_contains_anagrams(str_list):
    anagrams_dict = dict()
    for word in str_list:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if word in anagrams_dict:
                anagrams_dict[word] += 1
            else:
                anagrams_dict[word] = 1
    count_pairs = sum([value * (value - 1) // 2 for value in anagrams_dict.values()])
    if count_pairs <= 65:
        return True
    else:
        return False
