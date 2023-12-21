
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    dict_lst = ["".join(sorted(word.lower())) for word in lst if len(word)>=3]
    freq_dict = Counter(dict_lst)
    for freq in freq_dict.values():
        count += (freq*(freq-1)) // 2

    if count >= 40:
        return True
    else:
        return False
