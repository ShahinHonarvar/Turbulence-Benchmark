
from collections import defaultdict

def if_contains_anagrams(lst):
    count_dict = defaultdict(int)

    for string in lst:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            count_dict[sorted_string] += 1

    anagram_pairs = sum(value-1 for value in count_dict.values())

    return anagram_pairs >= 44
