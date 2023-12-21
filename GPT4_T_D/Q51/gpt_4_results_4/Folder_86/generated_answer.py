
from collections import Counter

def if_contains_anagrams(string_list):
    anagram_counter = 0
    string_list = [''.join(sorted(string.lower())) for string in string_list if len(string) >= 3]

    for string in string_list:
        anagram_counter += sum(1 for i in string_list if i == string)

    return anagram_counter // 2 <= 48
