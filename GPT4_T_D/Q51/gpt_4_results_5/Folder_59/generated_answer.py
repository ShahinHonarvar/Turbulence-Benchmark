
from collections import defaultdict

def if_contains_anagrams(lst):
    # Create a dictionary with sorted string as keys and their permutations as values
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)

    # Check the number of anagram pairs
    counter = 0
    for word_list in anagram_dict.values():
        anagram_count = len(word_list)
        if anagram_count > 1:
            counter += anagram_count * (anagram_count - 1) // 2

    return counter <= 15
