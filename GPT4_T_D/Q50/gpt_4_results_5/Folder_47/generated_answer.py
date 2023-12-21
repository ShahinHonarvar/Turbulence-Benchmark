
from collections import Counter

def if_contains_anagrams(strings_list):
    frequency_counter = Counter([''.join(sorted(x.lower())) for x in strings_list if len(x) >= 3])
    pairs_counter = sum([int(val*(val-1)/2) for val in frequency_counter.values()])
    return pairs_counter >= 47
