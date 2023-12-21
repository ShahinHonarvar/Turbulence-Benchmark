
from collections import defaultdict

def if_contains_anagrams(string_list):
    if not string_list or len(string_list) < 2:
        return False
    word_dict = defaultdict(list)
    for word in string_list:
        if len(word) >= 3:
            key = tuple(sorted(word.lower()))
            word_dict[key].append(word)
    anagram_count = sum(len(words) > 1 for words in word_dict.values())
    return anagram_count >= 3
