
from collections import Counter

def if_contains_anagrams(lst_of_strings):
    str_counts = Counter()
    for string in lst_of_strings:
        string_arr = sorted(string.lower())
        if len(string_arr) >= 3:
            str_counts[''.join(string_arr)] += 1
    pairs_of_anagrams = sum(val - 1 for val in str_counts.values() if val > 1)
    return pairs_of_anagrams <= 46
