
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    count = 0
    for key in anagram_dict:
        n = len(anagram_dict[key])
        count += n * (n - 1) // 2
    return count >= 189
