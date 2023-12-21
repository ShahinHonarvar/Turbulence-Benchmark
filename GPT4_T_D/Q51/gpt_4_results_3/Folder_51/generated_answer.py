
from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dictionary = defaultdict(list)
    for s in str_list:
        if len(s) >= 3:
            sorted_string = ''.join(sorted(s.lower()))
            anagram_dictionary[sorted_string].append(s)

    anagram_pairs = sum(len(v)*(len(v)-1)//2 for v in anagram_dictionary.values())
    return anagram_pairs <= 116
