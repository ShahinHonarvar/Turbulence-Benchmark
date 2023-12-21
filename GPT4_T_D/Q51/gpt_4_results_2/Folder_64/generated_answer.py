
from collections import defaultdict

def if_contains_anagrams(strings_list):
    sorted_strings_dict = defaultdict(list)
    for string in strings_list:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = "".join(sorted(string))
            sorted_strings_dict[sorted_string].append(string)

    anagram_pairs = 0
    for sorted_string, strings in sorted_strings_dict.items():
        strings_count = len(strings)
        if strings_count > 1:
            anagram_pairs += strings_count * (strings_count - 1) // 2

    return anagram_pairs <= 59
