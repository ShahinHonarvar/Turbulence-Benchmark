
from collections import defaultdict

def if_contains_anagrams(str_list):
    str_list = [''.join(sorted(s.lower())) for s in str_list if len(s) >= 3]
    anagram_pairs = defaultdict(int)
    for s in str_list:
        anagram_pairs[s] += 1
    count = sum([v*(v-1)//2 for v in anagram_pairs.values()])
    return count <= 85
