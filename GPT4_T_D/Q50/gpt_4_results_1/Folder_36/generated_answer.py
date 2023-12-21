
from itertools import combinations

def if_contains_anagrams(list_of_strings):
    
    def check_if_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    possible_pairs = list(combinations(list_of_strings, 2))
    anagram_pairs = [pair for pair in possible_pairs if len(pair[0]) >= 3 and len(pair[1]) >= 3 and check_if_anagram(pair[0], pair[1])]

    return len(anagram_pairs) >= 312
