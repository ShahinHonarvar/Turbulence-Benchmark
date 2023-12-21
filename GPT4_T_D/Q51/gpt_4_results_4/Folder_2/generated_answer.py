
from collections import defaultdict

def if_contains_anagrams(string_list):
    string_list = [s.lower() for s in string_list if len(s) >= 3]
    word_dict = defaultdict(int)

    for string in string_list:
        sorted_string = ''.join(sorted(string))
        word_dict[sorted_string] += 1

    pair_count = sum(val * (val-1) // 2 for val in word_dict.values())

    return pair_count <= 81
