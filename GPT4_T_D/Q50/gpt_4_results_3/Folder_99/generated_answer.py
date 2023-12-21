
from collections import defaultdict

def if_contains_anagrams(strings):
    # Dictionary where sorted strings are keys and original strings are values
    anagram_dict = defaultdict(list)

    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string].append(string)

    # Counting the number of pairs of anagrams
    anagram_pairs = sum(len(value_list) * (len(value_list) - 1) // 2 for value_list in anagram_dict.values())
    
    return anagram_pairs >= 314
