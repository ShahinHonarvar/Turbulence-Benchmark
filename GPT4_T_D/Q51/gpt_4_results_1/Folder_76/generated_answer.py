
from collections import Counter

def if_contains_anagrams(string_list):
    string_list = ["".join(sorted([char.lower() for char in string])) for string in string_list if len(string) >= 3]
    freq_dict = Counter(string_list)
    anagram_pairs_count = sum([count*(count-1)//2 for count in freq_dict.values()])
    return anagram_pairs_count <= 91
