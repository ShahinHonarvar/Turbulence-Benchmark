
from collections import Counter

def if_contains_anagrams(s_list):
    s_list = [''.join(sorted(list(s.lower()))) for s in s_list if len(s) >= 3]
    anagrams = [val for val in Counter(s_list).values() if val > 1]
    pairs = sum(map(lambda n: n * (n - 1) // 2, anagrams))
    return pairs >= 153
