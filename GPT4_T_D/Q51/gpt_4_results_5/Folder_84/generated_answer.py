
from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_groups = defaultdict(list)

    for string in string_list:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            anagram_groups[key].append(string)

    anagram_pairs_count = sum(len(strings)*(len(strings)-1)//2 for strings in anagram_groups.values())

    return anagram_pairs_count <= 16
