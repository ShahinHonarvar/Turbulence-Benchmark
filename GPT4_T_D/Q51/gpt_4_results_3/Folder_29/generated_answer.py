
from collections import defaultdict

def if_contains_anagrams(string_list):
    string_dict = defaultdict(list)
    anagram_pairs = 0

    for string in string_list:
        key = "".join(sorted(string.lower()))
        if len(key) >= 3:
            string_dict[key].append(string)

    for k, v in string_dict.items():
        anagram_pairs += len(v) * (len(v) - 1) // 2
        if anagram_pairs > 318:
            return False

    return True
