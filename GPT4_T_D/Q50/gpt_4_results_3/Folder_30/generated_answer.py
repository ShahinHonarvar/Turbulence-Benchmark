
from collections import Counter

def if_contains_anagrams(lst):
    cnt = 0
    str_dict = ["".join(sorted(word.lower())) for word in lst if len(word) >= 3]
    freq_dict = Counter(str_dict)
    for value in freq_dict.values():
        cnt += value * (value - 1) // 2
    return cnt >= 78
