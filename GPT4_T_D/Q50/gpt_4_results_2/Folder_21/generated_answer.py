
def if_contains_anagrams(string_list):
    from collections import defaultdict
    from itertools import combinations

    anagram_dict = defaultdict(list)
    for string in string_list:
        if len(string) >= 3:
            sorted_str = "".join(sorted(string.lower()))
            anagram_dict[sorted_str].append(string)

    anagram_pairs_count = sum(len(list(combinations(value, 2))) for value in anagram_dict.values())

    return anagram_pairs_count >= 136
