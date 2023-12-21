
from collections import defaultdict

def if_contains_anagrams(lst):
    word_dict = defaultdict(list)
    for word in lst:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) > 2:
            word_dict[sorted_word].append(word)
    anagram_pairs = sum(len(values)*(len(values)-1)//2 for values in word_dict.values())
    return anagram_pairs <= 72
