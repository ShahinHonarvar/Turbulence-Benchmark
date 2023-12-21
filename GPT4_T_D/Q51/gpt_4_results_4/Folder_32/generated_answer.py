
from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_pairs = defaultdict(set)
    anagram_count = 0
    
    for string in string_list:
        sorted_str = "".join(sorted(string.lower()))
        if len(sorted_str) < 3:
            continue
        else:
            if sorted_str in anagram_pairs:
                anagram_pairs[sorted_str].add(string)
                if len(anagram_pairs[sorted_str]) > 1:
                    anagram_count += 1
            else:
                anagram_pairs[sorted_str].add(string)
    
    if anagram_count <= 89:
        return True
    else:
        return False
