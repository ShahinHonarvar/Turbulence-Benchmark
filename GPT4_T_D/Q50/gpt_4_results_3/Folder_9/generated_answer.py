
from collections import Counter

def if_contains_anagrams(lst):
    hash_map = {}
    for string in lst:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if sorted_string in hash_map:
                hash_map[sorted_string] += 1
            else:
                hash_map[sorted_string] = 1

    pairs_counter = sum([Counter([item])[i]//2 for i in Counter([item])])
    return pairs_counter >= 66
