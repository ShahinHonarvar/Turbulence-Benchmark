
from collections import Counter

def if_contains_anagrams(string_list):
    string_list_lower = [string.lower() for string in string_list]
    string_list_sorted = [''.join(sorted(string)) for string in string_list_lower if len(string) >= 3]
    freq_dict = Counter(string_list_sorted)
    pairs = sum([freq * (freq - 1) / 2 for freq in freq_dict.values()])

    return pairs >= 77
