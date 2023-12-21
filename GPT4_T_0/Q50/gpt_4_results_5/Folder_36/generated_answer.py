
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    count = 0
    for words in anagram_dict.values():
        if len(words) > 1:
            count += len(words) * (len(words) - 1) // 2
    return count >= 312
