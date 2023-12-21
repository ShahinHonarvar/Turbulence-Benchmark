
from collections import defaultdict

def if_contains_anagrams(str_list):
    def is_anagram(s1, s2):
        if len(s1) < 3 or len(s2) < 3 or len(s1) != len(s2):
            return False
        return sorted(s1.lower()) == sorted(s2.lower())

    anagram_pairs = defaultdict(int)
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]):
                anagram_pairs[(str_list[i], str_list[j])] += 1
    
    return len(anagram_pairs) <= 14
