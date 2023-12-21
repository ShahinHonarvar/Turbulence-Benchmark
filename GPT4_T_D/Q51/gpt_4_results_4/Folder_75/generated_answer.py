
from collections import defaultdict

def if_contains_anagrams(str_list):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    anagram_dict = defaultdict(list)
    for s in str_list:
        if len(s) >= 3:
            sorted_s = "".join(sorted(s.lower()))
            anagram_dict[sorted_s].append(s)
    
    pairs_count = sum(len(anagrams)*(len(anagrams)-1)//2 for anagrams in anagram_dict.values() if len(anagrams) > 1)

    return pairs_count <= 55
