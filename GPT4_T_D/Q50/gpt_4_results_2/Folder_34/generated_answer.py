
from collections import Counter

def if_contains_anagrams(lst):
    str_dict = Counter([''.join(sorted(s.lower())) for s in lst if len(s) >= 3])
    anagram_count = sum([v*(v-1)//2 for v in str_dict.values()])
    return anagram_count >= 25
