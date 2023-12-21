
from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for string in str_list:
        key = "".join(sorted(string.lower()))
        if len(key) > 2:
            anagram_dict[key].append(string)
    pairs = sum([len(values)*(len(values)-1)//2 for values in anagram_dict.values()])
    return pairs <= 36
