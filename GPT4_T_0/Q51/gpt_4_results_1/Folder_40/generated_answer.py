
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_pairs = sum(len(values)*(len(values)-1)//2 for values in anagram_dict.values())
    return anagram_pairs <= 29
