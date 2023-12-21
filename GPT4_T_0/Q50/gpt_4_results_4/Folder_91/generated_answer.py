
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    count = 0
    for value in anagram_dict.values():
        if len(value) > 1:
            count += len(value) - 1
        if count >= 6:
            return True
    return False
