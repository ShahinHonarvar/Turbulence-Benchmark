
import collections

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = collections.defaultdict(int)

    for string in string_list:
        if len(string) >= 3 and string.isalpha():
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string] += 1

    for count in anagram_dict.values():
        if count >= 2:
            anagram_count += count // 2

    return anagram_count <= 3
