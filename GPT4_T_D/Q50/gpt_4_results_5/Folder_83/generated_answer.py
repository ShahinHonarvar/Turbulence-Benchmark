
from collections import Counter

def if_contains_anagrams(lst_string):
    string_counter = {}
    for string in lst_string:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in string_counter:
                string_counter[key] += 1
            else:
                string_counter[key] = 1
    anagram_pairs = sum((count*(count-1))//2 for count in string_counter.values())
    return anagram_pairs >= 48
