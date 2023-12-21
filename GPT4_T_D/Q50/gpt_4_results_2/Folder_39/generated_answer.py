
from collections import Counter

def if_contains_anagrams(list_of_strings):
    counted = Counter([''.join(sorted(word.lower())) for word in list_of_strings if len(word) >= 3])
    pair_count = sum((count * (count - 1)) // 2 for count in counted.values())
    return pair_count >= 54
