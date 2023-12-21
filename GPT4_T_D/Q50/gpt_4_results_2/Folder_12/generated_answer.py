
from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for i, word in enumerate(str_list):
        word = word.lower()
        sorted_word = "".join(sorted(word))
        if len(word) >= 3:
            anagram_dict[sorted_word].append(i)
    pair_count = 0
    for value in anagram_dict.values():
        n = len(value)
        if n > 1:
            pair_count += n * (n - 1) / 2
    if pair_count >= 69:
        return True
    else:
        return False
