
from collections import Counter

def if_contains_anagrams(str_list):
    anagram_pairs = []
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3:
                if Counter(str_list[i].lower()) == Counter(str_list[j].lower()):
                    anagram_pairs.append((str_list[i], str_list[j]))
    return len(anagram_pairs) <= 15
