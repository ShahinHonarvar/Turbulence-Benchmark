
from collections import defaultdict

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def if_contains_anagrams(list_of_strings):
    pairs_counter = 0
    hashmap = defaultdict(list)
    for word in list_of_strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            hashmap[sorted_word].append(word)
    
    for key in hashmap.keys():
        pairs_counter += len(hashmap[key]) * (len(hashmap[key]) - 1) // 2

    return pairs_counter <= 210
