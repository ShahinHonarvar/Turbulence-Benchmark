
from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [str_.lower() for str_ in str_list if len(str_) >= 3]
    freqs = Counter([''.join(sorted(str_)) for str_ in str_list])
    pairs = sum([freq * (freq - 1) // 2 for freq in freqs.values()])
    return pairs >= 40
