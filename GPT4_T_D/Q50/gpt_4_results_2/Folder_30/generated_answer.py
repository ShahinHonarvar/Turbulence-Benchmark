
from collections import Counter

def if_contains_anagrams(string_list):
    freq_dict = Counter([''.join(sorted(s.lower())) for s in string_list if len(s)>=3])

    pairs = sum(v * (v - 1) // 2 for v in freq_dict.values())

    return pairs >= 78
