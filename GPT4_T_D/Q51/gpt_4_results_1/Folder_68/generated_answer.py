
from collections import defaultdict

def if_contains_anagrams(string_list):
    def get_sorted(x):
        return ''.join(sorted(x.lower()))

    anagrams_dict = defaultdict(int)
    pairs = 0
    for string in string_list:
        if len(string) >= 3:
            sorted_string = get_sorted(string)
            pairs += anagrams_dict[sorted_string]
            anagrams_dict[sorted_string] += 1

    return pairs <= 94
